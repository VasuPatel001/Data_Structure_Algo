"""
Leetcode 256. Paint House
Medium

There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses. 

Example 1:
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

Example 2:
Input: costs = [[7,6,2]]
Output: 2

Constraints:
costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
"""


class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        # f[h][c] = Min cost way to paint all houses such that last house has color c
        # f[h][c] = min(f[h-1][c'], f[h-1][c"]) + f[h][c] ;  where c' and c" are other two colors
        if len(costs) == 0:
            return 0
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n)]

        dp[0] = costs[0]
        for house in range(1, len(costs)):
            dp[house][0] = min(dp[house-1][1], dp[house-1][2]) + costs[house][0]
            dp[house][1] = min(dp[house-1][0], dp[house-1][2]) + costs[house][1]
            dp[house][2] = min(dp[house-1][0], dp[house-1][1]) + costs[house][2]

        return min(dp[-1])
