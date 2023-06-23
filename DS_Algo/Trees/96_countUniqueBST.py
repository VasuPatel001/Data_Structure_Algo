"""
Leetcode 96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 19
"""

"""
This question is similar to Catalan number = (1/ (n+1)) * (2n C n)
Time Complexity: total number of leaf nodes in Catalan's number (equal to above formula), 
hence time complexity is O(2^n * n) because we are choosing 'n' different root element and 
2^n because there are 2 recursive calls being made with each 

Space complexity: max call step depth = O(n)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = {}  # this is the important DP problem
        
        def helper(n: int):
            total = 0
            # memoization
            if n in self.memo: return self.memo[n]
            
            # leaf node worker
            if n == 1 or n == 0:
                self.memo[0] = 1
                self.memo[1] = 1
                return 1

            # internal node worker
            for i in range(1, n+1):
                total += (helper(i-1) * helper(n-i))
            self.memo[n] = total
            return total

        return helper(n)