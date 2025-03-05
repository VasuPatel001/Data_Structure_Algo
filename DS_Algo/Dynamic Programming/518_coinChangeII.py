"""
Leetcode 518. Coin Change II

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # Method 3: Systematic way of doing it (using IK method of 2D DP table)

        dp = [[0 for _ in range(1+amount)] for _ in range(1+len(coins))]

        # init col=0 (having amount=0) to 1, since there's only 1 way to make amount=0, i.e. not taking any coin
        for row in range(1, 1+len(coins)):
            dp[row][0] = 1

        for coin in range(1, len(coins)+1):
            for amt in range(1, amount+1):
                if amt - coins[coin-1] >= 0:
                    dp[coin][amt] = dp[coin-1][amt] + dp[coin][amt-coins[coin-1]]
                else:
                    dp[coin][amt] = dp[coin-1][amt]

        return dp[coin][amount]

        ##############################
        dp = [0] * (amount + 1)
        dp[0] = 1

        # Method 1:
        # IMP: looping over coins from l->r or r->l doesn't make a difference
        for coin in coins:
            for target in range(1, amount+1):
                if target - coin >= 0:
                    dp[target] += dp[target - coin]

        # Method 2:
        # for i in range(len(coins)-1, -1, -1):
        #     for target in range(1, amount+1):
        #         if target - coins[i] >= 0:
        #             dp[target] += dp[target - coins[i]]

        return dp[amount]
