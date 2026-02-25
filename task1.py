import time
from typing import Callable, Dict

#Нотатка пану Кирилу: Я розумію, що в умові було зробити дещо легшим способом, але хочу попрактикувати кастомні докоратори

def cached(func: Callable):
    cache:Dict[int, int] = {}
    def wrapper(*args, **kwargs):
        input_arg = int(*args)
        if input_arg not in cache:
            result = func(*args, **kwargs)
            cache[input_arg] = result
            return result
        else:
            return cache[input_arg]
    return wrapper

@cached
def fibonacci(x: int) -> int:
    if x <= 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)


before = time.time_ns()
print(fibonacci(15))
after = time.time_ns()
print("TI", (after - before))

before2 = time.time_ns()
print(fibonacci(15))
after2 = time.time_ns()
print("TI", (after2 - before2))