from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    result = {1: 0, 2: 1}
    def fibonacci(n: int) -> int:
        if n in result:
            return result[n]
        else:
            result[n] = fibonacci(n-1) + fibonacci(n-2)
            return result[n]
    return fibonacci



test_function = caching_fibonacci()
print(test_function(5))
print(test_function(3))
print(test_function(15))
print(test_function(50))
print(test_function(20))