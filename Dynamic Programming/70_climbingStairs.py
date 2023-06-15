"""
Leetcode 70: Climbing Stairs OR Count Ways To Reach The Nth Step
https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484805-923140-57-347

Count Ways To Reach The Nth Step
There is a staircase with n steps. A person standing at the 0-th step wants to reach the n-th one. They are capable of jumping up by certain numbers of steps at a time.
Given how the person can jump, count the number of ways they can reach the top.

Example One
{"steps": [1, 2],
"n": 1}
Output:
1
The person can jump up by either 1 or 2 steps at a time. The only way to reach step 1 from step 0 is to jump up one step once.

Example Two
{"steps": [1, 2],
"n": 2}
Output:
2
There are two distinct ways to reach step 2: {1, 1}, {2}.

Example Three
{"steps": [2, 3],
"n": 7}
Output:
3
There are three distinct ways to reach step 7 from step 0: {2, 2, 3}, {2, 3, 2}, {3, 2, 2}.

Notes
Constraints:
1 <= n <= 10000
1 <= length of the given list steps <= 100
1 <= element of the given list steps <= 10000
Answer will fit in a 64-bit integer
"""

"""
Time complexity: O(n*len(steps))
Space: Compexity: O(n)
"""


def count_ways_to_climb(steps, n):
    """
    Args:
     steps(list_int32)
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    dp_list = [0] * (n + 1)
    dp_list[0] = 1
    
    for i in range(1, n+1):
        for step in steps:
            if i - step >= 0:
                dp_list[i] += dp_list[i-step]
    
    return dp_list[n]