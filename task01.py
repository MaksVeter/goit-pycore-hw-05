from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(n: int) -> int:
        if (n in cache):
            return cache[n]
        if (n <= 1):
            return n
        cache[n] = fibonacci(n-1)+fibonacci(n-2)
        return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(3))  # Виведе 2
print(fib(3))  # Виведе 2
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
