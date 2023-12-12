import logging
import io
import json
import time
from termcolor import colored
from contextlib import contextmanager
import smtplib
from email.mime.text import MIMEText

def load_config(file_path: str) -> dict:
    """
    Loads a json configuration file.

    Args:
        file_path (str): The path to the configuration file.

    Returns:
        dict: The configuration settings.
    """
    with open(file_path, 'r') as f:
        return json.load(f)
    
def setup_logging() -> io.StringIO:
    """
    Sets up logging to both the console and a StringIO object.

    Returns:
    StringIO: The StringIO object that logging output is written to
    """
    log_stream = io.StringIO()

    # Set up logging to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s- %(message)s'))

    # Set up logging to StringIO object
    stream_handler = logging.StreamHandler(log_stream)
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s- %(message)s'))

    # Get the root logger and add the handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(stream_handler)

    return log_stream

def handle_exception(e, attempt, max_attempts):
    """
    Handles exceptions, specifically for failed connections.

    This function logs an error message indicating the failed connection attempt number.
    If the current attempt number is less than the maximum number of attempts minus one,
    the function pauses execution for 5 seconds before the next connection attempt is made.
    If all connection attempts have failed, the function logs an error messge and re-raises the last exception.

    Args:
        e (Exception): The exception that was raised.
        attempt (int): The current attempt number (zero-indexed).
        max_attempts (int): The maximum number of attempts that should be made.

    Raises:
        Exception: The same exception that was passed in if all connection attempts have failed.

    Returns:
        None
    """
    logging.error(f"Connection failed on attempt {attempt+1}")
    if attempt < max_attempts - 1:
        time.sleep(5)
    else:
        logging.error("All connection attempts failed")
        raise

def send_log_email(long_stream, config):
    long_stream.seek(0)
    send_email(config['subject'], long_stream.read(), config['email_sender'], config['email_receipt'])

def reset_log_stream(log_stream):
    log_stream.truncate(0)
    log_stream.seek(0)

def send_email(subject: str, body: str, sender: str, recipients: list) -> None:
    """
    Sends an email.

    Parameters:
        subject (str): The subject of the email.
        body (str): The body of the email.
        sender (str): The email address of the sender.
        recipients (list): A list of email addresses to send the email to.

    Returns:
        None
    """
    # Create a MIMEText object with the email body
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # Send the email
    # Notes:
    #   - Run the following command to start a simple SMTP server listening on port 1025, printing the contents to the console for debugging purposes.
    #       'python -m smtpd -n -c DebuggingServer localhost: 1025'
    s = smtplib.SMTP('localhost', 1025)
    s.send_message(msg)
    s.quit()

@contextmanager
def timer(description: str) -> None:
    """
    A context manager for timing a block of code.

    This function logs the time taken to execute the code inside the context block.
    The time is logged in minutes.

    Args:
        description (str): A description of the code being timed. This will be included in the log message.

    Yields:
        None
    """
    start = time.time()
    yield # Yield control back to the context block
    elapsed = (time.time() - start) / 60
    color = get_color(elapsed)

    logging.info(f"{description}: {colored(f'{elapsed:.2f}', color)} minutes")

def get_color(elapsed: float) -> str:
    if elapsed > 10:
        return 'red'
    elif elapsed > 5:
        return 'yellow'
    else:
        return 'green'