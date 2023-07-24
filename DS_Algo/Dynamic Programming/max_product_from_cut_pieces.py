"""
Cut The Rope
IK DP Test question: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484808-924352-59-358

Given a rope, cut it into parts maximizing the product of their lengths.
Example
{"n": 4}
Output:
4
Length of the rope is 4.
All ways it can be cut into parts: 1+3, 1+1+2, 1+1+1+1, 2+2, 2+1+1.
Among these, 2+2 cut makes for the greatest product: 2*2=4.

Notes
Return an integer which equals to the maximum possible product of the given rope’s parts.
Constraints:

2 <= length of the rope <= 94
You have to cut at least once.
Length of the rope, lengths of all parts are all positive integers.
"""


def max_product_from_cut_pieces(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    dp = [1 for _ in range(n+1)]

    # base case
    # dp[0] = dp[1] = 1 stands for length 1

    if n == 2:
        return 1
    if n == 3:
        return 2

    for l in range(2, n+1):
        for c in range(1, l+1):
            dp[l] = max(dp[l], dp[l-c] * c)

    return dp[n]
