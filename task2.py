import re
from typing import Callable, List

FLOAT_PATTERN = r'(?<!\d)\d+\.\d+(?!\d)'
def generator_numbers(text: str):
    for m in re.finditer(FLOAT_PATTERN, text):
        yield float(m.group())

def sum_profit(text: str, generator: Callable):
    total_income = 0
    for number in generator(text):
        total_income += number
    return total_income


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")