
"""
This question is similar to Catalan number = (1/ (n+1)) * (2n C n)
Time Complexity: total number of leaf nodes in Catalan's number (equal to above formula), 
hence time complexity is O(2^n * n) because we are choosing 'n' different root element and 
2^n because there are 2 recursive calls being made with each 

Space complexity: max call step depth = O(n)
"""

def how_many_bsts(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    ans = 0
    
    if n == 0 or n == 1:
        return 1
    
    for i in range(1, n+1):
        ans = ans + (how_many_bsts(i - 1) * how_many_bsts(n - i))
    
    return ans