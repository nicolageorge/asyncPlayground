from math import sqrt
import time


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def async_is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        yield
    return True

def search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("Not Found")


def async_search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        yield
    raise ValueError("Not Found")


def async_print_matches(iterable, predicate):
    for item in iterable:
        matches = yield from predicate(item)
        if matches:
            print(f"Founid: {item}", end=", ")


def async_repetitive_message(message, interval_seconds):
    while True:
        print(message)
        start = time.time()
        expiry = start + interval_seconds
        while True:
            yield
            now = time.time()
            if now >= expiry:
                break

