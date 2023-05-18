"""
"""

def binaryStringN(n: int) -> list[str]:
    if n == 1:
        return ["0", "1"]
    
    prev = binaryStringN(n-1)
    result = []
    for s in prev:
        result.append(s+"0")
        result.append(s+"1")
    return result

