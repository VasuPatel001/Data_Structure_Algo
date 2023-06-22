"""
Number Of Ways To Make Change
Given a variety of coin denominations existing in a currency system, find the total number of ways a given amount of money can be expressed using coins in that currency system.
Assume infinite supply of coins of every denomination. Return answer modulo 1000000007.

Example
{"coins ": [1, 2, 3],
"amount": 3}
Output:
3

The three ways are:
Use the coin with denomination 1 three times.
Use the coin with denomination 3 once.
Use the coin with denomination 2 once and coin with denomination 1 once.

Notes
Two ways are considered different if they use a different number of coins of any particular denomination.

Constraints:
1 <= total number of denominations <= 102
1 <= denomination of a coin <= 104
1 <= amount to be expressed <= 104
"""


def number_of_ways(coins, amount):
    """
    Args:
     coins(list_int32)
     amount(int32)
    Returns:
     int32
    """
    # Write your code here.
    
    """
    Asymptotic complexity in terms of `n` = size of the input list and `amount`:
    Time: O(n * amount).
    Auxiliary space: O(n * amount).
    Total space: O(n * amount).
    """
    dp_table = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
    # base case initialization
    
    mod_val = 1000000007
    for row in range(len(coins)):
        for target in range(amount+1):
            if target == 0:
                dp_table[row][0] = 1
            else:
                if row > 0:
                    dp_table[row][target] = dp_table[row-1][target]
                
                if target - coins[row] >= 0:
                    dp_table[row][target] = (dp_table[row][target] + dp_table[row][target - coins[row]]) % mod_val
    
    return dp_table[len(coins)-1][amount]
    
    
    ##############################################
    """
    Memory optimization idea:
    In this problem there can be O(n * amount) different states. So the dp table that we are computing should
    be of the size n * amount. Let us call this dp table of size n * amount as the "complete dp table".

    The complete dp table can be thought as a table having "n" rows and "amount" columns. In our solution, we
    will fill up the table row by row. Notice that, while computing any cell of a row, we only need the
    information from the immediate previous row. So we do not need to store all the rows of the complete dp
    table during computing the table. Only the data of the immediate previous row and current row needs to be
    stored.

    Our optimized dp table has 2 rows and "amount" columns. We will be cyclically using these two rows to
    compute our solution. While computing the rows, the data of the i-th row from the complete dp table will
    be stored in (i % 2)-th row of our optimized dp table.
    """
    dp_table = [[0 for _ in range(amount+1)] for _ in range(2)]
    # base case initialization
    
    mod_val = 1000000007
    for row in range(len(coins)):
        for target in range(amount+1):
            if target == 0:
                dp_table[row%2][0] = 1
            else:
                if row > 0:
                    dp_table[row%2][target] = dp_table[(row-1)%2][target]
                
                if target - coins[row] >= 0:
                    dp_table[row%2][target] = (dp_table[row%2][target] + dp_table[row%2][target - coins[row]]) % mod_val
    
    return dp_table[(len(coins)-1)%2][amount]
    