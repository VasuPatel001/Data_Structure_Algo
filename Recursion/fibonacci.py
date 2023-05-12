def fibonacci(n:int, b1: int, b2: int) -> int:
    if n ==0:
        return b1
    return fibonacci(n-1, b2, b1 + b2)