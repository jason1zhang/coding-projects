from Hanoi import Hanoi
from StringReversal import StringReversal
import logging

# 创建一个logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
file_handler = logging.FileHandler("./app.log")
file_handler.setLevel(logging.DEBUG)

# 创建一个formatter，用于设定日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(file_handler)

# 定义一个生成器函数，用于生成斐波那契数列
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 在调用原始函数之前的操作
        print("Before calling the function")

        result = func(*args, **kwargs)

        # 在调用原始函数之后的操作
        print("After calling the function")
        return result
    return wrapper

@my_decorator
def my_function(name):
    print(f"Hello, {name}!")

def logged(prefix: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Entering {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{prefix}: Exiting {func.__name__}")
            return result
        return wrapper
    return decorator

@logged("DEBUG")
def add(a, b):
    return a + b

def log_decorator(func):
    def wrapper(*args, **kwargs):
        # 记录函数调用前的日志
        logger.info(f"Calling function {func.__name__} with arguments {args}, {kwargs}")

        # 调用原始函数并获取结果
        result = func(*args, **kwargs)

        # 记录函数调用后的日志
        logger.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    # Driver code
    # s = "hello"
    # print(StringReversal.reverse_string_2(s))

    """
    disks = int(input("Number of disks to be displaced: "))
    Hanoi.hanoi(disks, 'A', 'B', 'C')
    """

    # demo of generator
    even_squares_gen = (x**2 for x in range(10) if x % 2 == 0)

    # for square in even_squares_gen:
        # print(square)
    
    print(next(even_squares_gen))
    print(next(even_squares_gen))


    # 创建一个包含数百万个元素的大列表
    large_list = list(range(10000000))

    # 使用迭代器遍历前10个元素
    iterator = iter(large_list)
    for _ in range(10):
        print(next(iterator))

    # 使用生成器生成并打印前10个斐波那契数
    fib_generator = fibonacci_sequence(10)
    for num in fib_generator:
        print(num)

    my_function("Alice")

    print(add(3, 5))



    result1 = add(3, 5)
    result2 = multiply(4, 6)

    print(result1)  # 输出：8
    print(result2)  # 输出：24

    numbers = [1, 3, 6]
    newNumbers = tuple(map(lambda x: x, numbers))
    print(newNumbers)