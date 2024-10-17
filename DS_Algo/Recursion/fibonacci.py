"""
Time Complexity:
    O(n)

Space Complexity:
    output, aux: O(1)
    recursive call stack: O(n)
"""

def fibonacci(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = 6
    print(fibonacci(n))
