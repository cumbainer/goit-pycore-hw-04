import time
from typing import Callable, Dict

#Нотатка пану Кирилу: Я розумію, що в умові було зробити дещо легшим способом, але хочу попрактикувати кастомні докоратори

def cached(func: Callable):
    cache:Dict[int, int] = {}
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result not in cache:
            cache[result] = func(*args, **kwargs)
        return result
    return wrapper

@cached
def fibonacci(x: int) -> int:
    if x <= 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)


before = time.time_ns()
print(fibonacci(15))
after = time.time_ns()
print(after - before)

before2 = time.time_ns()
print(fibonacci(15))
after2 = time.time_ns()
print(after2 - before2)