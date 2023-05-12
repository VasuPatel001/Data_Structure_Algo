def combination(n: int, k: int) -> int:
    if n <= 0 or k == n or k == 0:
        return 1
    return combination(n-1, k-1) + combination(n-1, k) # where combination(n-1, k-1) is selection made
                                                       # where combination(n-1, k) is selection not made