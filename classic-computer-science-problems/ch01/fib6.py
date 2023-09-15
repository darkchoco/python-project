

# from typing import Generator
from collections.abc import Iterator

# def fib6(n: int) -> Generator[int, None, None]:
def fib6(n: int) -> Iterator:
    yield 0  # special case
    if n > 0: yield 1  # special case
    last_val: int = 0  # initially set to fib(0)
    next_val: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last_val, next_val = next_val, last_val + next_val
        yield next_val  # main generation step


if __name__ == "__main__":
    for i in fib6(50):
        print(i)
