"""
BFS Recursive Approach using 
Time complexity: O(N * 2^n): 2^n total nodes and each string concatenation take O(N) time.
Space complexity: O(N * 2^n) becuase result list keeps on appending 2^n solution and each string in N long.
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

