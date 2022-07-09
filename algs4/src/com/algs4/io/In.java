package com.algs4.io;

import java.io.*;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import java.util.*;
import java.util.regex.Pattern;

public final class In {
    // assume Unicode UTF-8 encoding
    private static final String CHARSET_NAME = "UTF-8";

    // assume language = English, country = US for consistency with System out
    private static final Locale LOCALE = Locale.US;

    // the default token separator; we maintain the invariant that this value
    // is held by the scanner's delimiter between calls
    private static final Pattern WHITESPACE_PATTERN = Pattern.compile("\\p{javaWhitespace}+");

    // make whitespace significant
    private static final Pattern EMPTY_PATTERN = Pattern.compile("");

    // used to read the entire input
    private static final Pattern EVERYTHING_PATTERN = Pattern.compile("\\A");

    private Scanner scanner;

    /**
     * Initializes an input stream from standard input.
     */
    private In() {
        scanner = new Scanner(new BufferedInputStream(System.in), CHARSET_NAME);
        scanner.useLocale(LOCALE);
    }

    /**
     * Initializes an input stream from a socket.
     *
     * @param socket the socket
     * @throws IllegalArgumentException if cannot open {@code socket}
     * @throws IllegalArgumentException if {@code socket} is {@code null}
     */
    public In(Socket socket) {
        if (socket == null) {
            throw new IllegalArgumentException("socket argument is null");
        }

        try {
            InputStream is = socket.getInputStream();
            scanner = new Scanner(new BufferedInputStream(is), CHARSET_NAME);
            scanner.useLocale(LOCALE);
        }
        catch (IOException ioe) {
            throw new IllegalArgumentException("Could not open " + socket, ioe);
        }
    }

    /**
     * Initializes an input stream from a URL.
     *
     * @param url the URL
     * @throws IllegalArgumentException if cannot open {@code url}
     * @throws IllegalArgumentException if {@code url} is {@code null}
     */
    public In(URL url) {
        if (url == null) {
            throw new IllegalArgumentException("url argument is null");
        }

        try {
            URLConnection site = url.openConnection();
            InputStream is = site.getInputStream();
            scanner = new Scanner(new BufferedInputStream(is), CHARSET_NAME);
            scanner.useLocale(LOCALE);
        }
        catch (IOException ioe) {
            throw new IllegalArgumentException("Could not open " + url, ioe);
        }
    }

    /**
     * Initializes an input stream from a file.
     *
     * @param file the file
     * @throws IllegalArgumentException if cannot open {@code file}
     * @throws IllegalArgumentException if {@code file} is {@code null}
     */
    public In(File file) {
        if (file == null) {
            throw new IllegalArgumentException("file argument is null");
        }

        try {
            // for consistency with StdIn, wrap with BufferedInputStream instead of use
            // file as argument to Scanner
            FileInputStream fis = new FileInputStream(file);
            scanner = new Scanner(new BufferedInputStream(fis), CHARSET_NAME);
            scanner.useLocale(LOCALE);
        }
        catch (IOException ioe) {
            throw new IllegalArgumentException("Could not open " + file, ioe);
        }
    }

    public In(String name) {
        if (name == null) {
            throw new IllegalArgumentException("argument is null");
        }
        if (name.length() == 0) {
            throw new IllegalArgumentException("argument is the empty string");
        }

        try {
            // first try to read file from local file system
            File file = new File(name);
            if (file.exists()) {
                // for consistency with StdIn, wrap with BufferedInputStream instead of use
                // file as argument to Scanner
                FileInputStream fis = new FileInputStream(file);
                scanner = new Scanner(new BufferedInputStream(fis), CHARSET_NAME);
                scanner.useLocale(LOCALE);
                return;
            }

            // resource relative to .class file
            URL url = getClass().getResource(name);

            // resource relative to classloader root
            if (url == null) {
                url = getClass().getClassLoader().getResource(name);
            }

            // or URL from web
            if (url == null) {
                url = new URL(name);
            }
            URLConnection site = url.openConnection();

            // in order to set User-Agent, replace above line with these two
            // HttpURLConnection site = (HttpURLConnection) url.openConnection();
            // site.addRequestProperty("User-Agent", "Mozilla/4.76");

            InputStream is = site.getInputStream();
            scanner = new Scanner(new BufferedInputStream(is), CHARSET_NAME);
            scanner.useLocale(LOCALE);
        }
        catch (IOException ioe) {
            throw new IllegalArgumentException("Could not open " + name, ioe);
        }
    }

    /**
     * Initializes an input stream from a given {@link Scanner} source, use with
     * {@code new Scanner(String)} to read from a string.
     * <p>
     * Note that this does not create a defensive copy, so the
     * scanner will be mutated as you read on.
     *
     * @param scanner the scanner
     * @throws IllegalArgumentException if {@code scanner} is {@code null}
     */
    public In(Scanner scanner) {
        if (scanner == null) {
            throw new IllegalArgumentException("scanner argument is null");
        }

        this.scanner = scanner;
    }

    /**
     * Returns true if this input stream exists.
     *
     * @return {@code true} if this input stream exists; {@code false} otherwise
     */
    public boolean exists() {
        return scanner != null;
    }

    /**
     * Return true if standard input is empty (except possibly for whitespace).
     * Use this method to know whether the next call to {@link @readString()},
     * {@link #readDouble()}, etc will succeed.
     *
     * @return {@code true} if standard input is empty (except possibly for
     *          whitespace); {@code false} otherwise
     */
    public boolean isEmpty() {
        return !scanner.hasNext();
    }

    /**
     * Return true if standard input has a next line.
     * Use this method to know whether the
     * next call to {@link #readLine()} will succeed.
     * This method is functionally equivalent to {@link #hasNextChar()}.
     *
     * @return {@code true} if standard input has more input (including whitespace);
     *          {@code false} otherwise
     */
    public boolean hasNextLine() {
        return scanner.hasNextLine();
    }

    /**
     * Returns true if this input stream has more input (including whitespace).
     * Use this method to know whether the next call to {@link #readChar()} will succeed.
     * This method is functionally equivalent to {@link #hasNextLine()}.
     *
     * @return {@code true} if this input stream has more input (including whitespace);
     *          {@code false} otherwise
     */
    public boolean hasNextChar() {
        scanner.useDelimiter(EMPTY_PATTERN);
        boolean result = scanner.hasNext();
        scanner.useDelimiter(WHITESPACE_PATTERN);
        return result;
    }

    /**
     * Reads and returns the next line in this input stream.
     *
     * @return the next line in this input stream; {@code null} if no such line
     */
    public String readLine() {
        String line;
        try {
            line = scanner.nextLine();
        } catch (NoSuchElementException e) {
            line = null;
        }

        return line;
    }

    /**
     * Reads and returns the next character in this input stream.
     *
     * @return the next {@code char} in this input stream
     * @throws NoSuchElementException if standard input is empty
     */
    public char readChar() {
        try {
            scanner.useDelimiter(EMPTY_PATTERN);
            String ch = scanner.next();
            assert ch.length() == 1 : "Internal (Std)In.readChar() error!"
                    + "Please contact the authors.";
            scanner.useDelimiter(WHITESPACE_PATTERN);
            return ch.charAt(0);
        } catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read a 'char' value from standard input,"
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads and returns the remainder of the inupt, as a string.
     *
     * @return the remainder of teh input, as a string
     */
    public String readAll() {
        if (!scanner.hasNextLine()) {
            return "";
        }

        String result = scanner.useDelimiter(EVERYTHING_PATTERN).next();
        // not that important to reset delimiter, since now scanner is empty
        scanner.useDelimiter(WHITESPACE_PATTERN);   // but let's do it anyway
        return result;
    }

    /**
     * Reads the next token from standard input and returns it as a {@code String}.
     *
     * @return the next {@code String} in this input stream
     * @throws NoSuchElementException if standard input is empty
     */
    public String readString() {
        try {
            return scanner.next();
        } catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read a 'String' value from standard input, "
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads the next token from this input stream, parses it as a {@code int},
     * and returns the {@code int}.
     *
     * @return the next integer on standard input
     * @throws NoSuchElementException if standard input is empty
     * @throws InputMismatchException if the next token cannot be parsed as an {@code int}
     */
    public int readInt() {
        try {
            return scanner.nextInt();
        }
        catch (InputMismatchException e) {
            String token = scanner.next();
            throw new InputMismatchException("atempts to read an 'int' value from standard input, "
                    + "but the next token is \"" + token + "\"");
        }
        catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read an 'int' value from standard input, "
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads the next token from standard input, parses it as a {@code double},
     * and returns the {@code double}.
     *
     * @return the next double on standard input
     * @throws NoSuchElementException if standard input is empty
     * @throws InputMismatchException if the next token cannot be parsed as an {@code double}
     */
    public double readDouble() {
        try {
            return scanner.nextDouble();
        }
        catch (InputMismatchException e) {
            String token = scanner.next();
            throw new InputMismatchException("attempts to read a 'double' value from standard input, "
                    + "but the next token is \"" + token + "\"");
        }
        catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read a 'double' value from standard input, "
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads the next token from standard input, parses it as a {@code float},
     * and returns the {@code float}.
     *
     * @return the next float on standard input
     * @throws NoSuchElementException if standard input is empty
     * @throws InputMismatchException if the next token cannot be parsed as an {@code float}
     */
    public float readFloat() {
        try {
            return scanner.nextFloat();
        }
        catch (InputMismatchException e) {
            String token = scanner.next();
            throw new InputMismatchException("attempts to read a 'float' value from standard input, "
                    + "but the next token is \"" + token + "\"");
        }
        catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read a 'float' value from standard input, "
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads the next token from standard input, parses it as a {@code long},
     * and returns the {@code long}.
     *
     * @return the next long on standard input
     * @throws NoSuchElementException if standard input is empty
     * @throws InputMismatchException if the next token cannot be parsed as an {@code long}
     */
    public long readLong() {
        try {
            return scanner.nextLong();
        }
        catch (InputMismatchException e) {
            String token = scanner.next();
            throw new InputMismatchException("attempts to read a 'long' value from standard input, "
                    + "but the next token is \"" + token + "\"");
        }
        catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read a 'long' value from standard input, "
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads the next token from standard input, parses it as a {@code short},
     * and returns the {@code short}.
     *
     * @return the next short on standard input
     * @throws NoSuchElementException if standard input is empty
     * @throws InputMismatchException if the next token cannot be parsed as an {@code short}
     */
    public short readShort() {
        try {
            return scanner.nextShort();
        }
        catch (InputMismatchException e) {
            String token = scanner.next();
            throw new InputMismatchException("attempts to read a 'short' value from standard input, "
                    + "but the next token is \"" + token + "\"");
        }
        catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read a 'short' value from standard input, "
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads the next token from standard input, parses it as a {@code byte},
     * and returns the {@code byte}.
     *
     * @return the next byte on standard input
     * @throws NoSuchElementException if standard input is empty
     * @throws InputMismatchException if the next token cannot be parsed as an {@code byte}
     */
    public byte readByte() {
        try {
            return scanner.nextByte();
        }
        catch (InputMismatchException e) {
            String token = scanner.next();
            throw new InputMismatchException("attempts to read a 'byte' value from standard input, "
                    + "but the next token is \"" + token + "\"");
        }
        catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read a 'byte' value from standard input, "
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads the next token from standard input, parses it as a {@code boolean},
     * and returns the {@code boolean}.
     *
     * @return the next boolean on standard input
     * @throws NoSuchElementException if standard input is empty
     * @throws InputMismatchException if the next token cannot be parsed as an {@code boolean};
     *      {@code true} or {@code 1} for true, and {@code false} or {@code 0} for false,
     *      ignoring case
     */
    public boolean readBoolean() {
        try {
            String token = readString();
            if("true".equalsIgnoreCase(token)) {
                return true;
            }
            if("false".equalsIgnoreCase(token)) {
                return false;
            }
            if("1".equals(token)) {
                return true;
            }
            if("0".equals(token)) {
                return false;
            }

            throw new InputMismatchException("attempts to read a 'boolean' value from standard input, "
                    + "but the next token is \"" + token + "\"");
        }
        catch (NoSuchElementException e) {
            throw new NoSuchElementException("attempts to read a 'boolean' value from standard input, "
                    + "but no more tokens are available");
        }
    }

    /**
     * Reads all remaining tokens from standard input and returns them as
     * an array of strings.
     *
     * @return all remaining tokens on standard input, as an array of strings
     */
    public String[] readAllStrings() {
        // we could use readAll.trim().split(), but that's not consistent
        // because trim() uses characters 0x00, 0x20 as whitespace
        String[] tokens = WHITESPACE_PATTERN.split(readAll());
        if (tokens.length == 0 || tokens[0].length() > 0) {
            return tokens;
        }

        // don't include first token if it is leading whitespace
        String[] decapitokens = new String[tokens.length - 1];
        System.arraycopy(tokens, 1, decapitokens, 0, tokens.length - 1);

        return decapitokens;
    }

    /**
     * Reads all remaining lines from standard input and returns them as
     * an array of strings.
     *
     * @return all remaining lines on standard input, as an array of strings
     */
    public String[] readAllLines() {
        ArrayList<String> lines = new ArrayList<>();
        while (hasNextLine()) {
            lines.add(readLine());
        }

        return lines.toArray(new String[lines.size()]);
    }

    /**
     * Reads all remaining tokens from standard input, parses them as integers,
     * and returns them as an array of integers.
     *
     * @return all remaining integers on standard input, as an array
     * @throws InputMismatchException if any token cannot be parsed as an {@code int}
     */
    public int[] readAllInts() {
        String[] fields = readAllStrings();
        int[] vals = new int[fields.length];
        for (int i = 0; i < fields.length; i++) {
            vals[i] = Integer.parseInt(fields[i]);
        }

        return vals;
    }

    /**
     * Reads all remaining tokens from standard input, parses them as longs,
     * and returns them as an array of longs.
     *
     * @return all remaining longs on standard input, as an array
     * @throws InputMismatchException if any token cannot be parsed as an {@code long}
     */
    public long[] readAllLongs() {
        String[] fields = readAllStrings();
        long[] vals = new long[fields.length];
        for (int i = 0; i < fields.length; i++) {
            vals[i] = Long.parseLong(fields[i]);
        }

        return vals;
    }

    /**
     * Reads all remaining tokens from standard input, parses them as doubles,
     * and returns them as an array of doubles.
     *
     * @return all remaining doubles on standard input, as an array
     * @throws InputMismatchException if any token cannot be parsed as an {@code double}
     */
    public double[] readAllDoubles() {
        String[] fields = readAllStrings();
        double[] vals = new double[fields.length];
        for (int i = 0; i < fields.length; i++) {
            vals[i] = Double.parseDouble(fields[i]);
        }

        return vals;
    }

    /**
     * Closes this input stream.
     */
    public void close() {
        scanner.close();
    }

    /**
     * Interactive test of basic functionality.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        In in;
        String urlName = "https://introcs.cs.princeton.edu/java/stdlib/InTest.txt";

        // read from a URL
        System.out.println("readAll() from URL" + urlName);
        System.out.println("---------------------------------------------------------------------------");
        try {
            in = new In(urlName);
            System.out.println(in.readAll());
        }
        catch (IllegalArgumentException e) {
            System.out.println(e);
        }
        System.out.println();

        // read one line at a time from URL
        System.out.println("readLine() from URL " + urlName);
        System.out.println("---------------------------------------------------------------------------");
        try {
            in = new In(urlName);
            while (!in.isEmpty()) {
                String s = in.readLine();
                System.out.println(s);
            }
        }
        catch (IllegalArgumentException e) {
            System.out.println(e);
        }
        System.out.println();
    }
}

