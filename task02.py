from typing import Callable
import re


def generator_numbers(text: str):

    search_pattern = r' -?\d+\.?\d* '
    for number in re.finditer(search_pattern, text):
        yield float(number.group().strip())


def sum_profit(text: str, func: Callable) -> float:
    sum = 0
    for number in generator_numbers(text):
        sum += number
    return sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

text2 = "Загальний дохід -78 працівника 55 складається з 0 декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text2, generator_numbers)
print(f"Загальний дохід: {total_income}")
