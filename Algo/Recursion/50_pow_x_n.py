"""
Leetcode 50: Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""


class Solution:
    ########################################################
    # Solution 1: x^n = (x^(n//2)) * (x ^ (n- (n//2)))
    ########################################################
    def myPow(self, x: float, n: int) -> float:
        hmap = {}
        if n < 0:
            return (1 / (self.helper(x, -n, hmap)))

        # n is positive
        return self.helper(x, n, hmap)

    def helper(self, x: float, n: int, hmap: dict) -> float:
        # memoization
        if n in hmap:
            return hmap[n]

        # Base cases
        if n == 1:
            hmap[1] = x
            return x
        if n == 0:
            hmap[0] = 1
            return 1
        hmap[n//2] = self.helper(x, (n//2), hmap)
        hmap[n-(n//2)] = (self.helper(x, (n - (n//2)), hmap))
        return hmap[n//2] * hmap[n-(n//2)]

    ########################################################
    # Solution 2: x^n = (x^2)^(n//2)
    ########################################################
    def myPow(self, x: float, n: int) -> float:

        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()

        return float(f) if n >= 0 else 1/f
