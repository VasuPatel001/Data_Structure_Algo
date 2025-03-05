"""
Leetcode 72. Edit Distance
Medium

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for row in range(1, m+1):
            dp[row][0] = row

        for col in range(1, n+1):
            dp[0][col] =col

        for row in range(1, m+1):
            for col in range(1, n+1):
                insert = dp[row-1][col] + 1
                delete = dp[row][col-1] + 1
                replace = dp[row-1][col-1]
                if word1[row-1] != word2[col-1]:
                    replace += 1

                dp[row][col] = min(insert, delete, replace)
        return dp[m][n]
