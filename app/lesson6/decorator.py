import random
import time


def timer(function):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        start_ts = time.time()
        result = function(*args, **kwargs)
        end_ts = time.time()
        print("Time: {} {}".format(function.__name__, (end_ts - start_ts) * 1000))
        return result
    return wrapper


def sleeper(from_, to):
    def _sleeper(function):
        def wrapper(*args, **kwargs):
            time.sleep(random.randint(from_, to))
            result = function(*args, **kwargs)
            return result
        return wrapper
    return _sleeper


@timer
@sleeper(1, 3)
def foo(a, b):
    return a + b


if __name__ == "__main__":
    print(foo(a=10,b=5))