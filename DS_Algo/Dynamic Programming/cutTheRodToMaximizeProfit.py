"""
Cut The Rod To Maximize Profit
IK Problem: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484806-923663-248-1565

Given the prices for rod pieces of every size between 1 inch and n inches, find the maximum total profit that can be made by cutting an n inches long rod inch into pieces.

Example
{
"price ": [1, 5, 8, 9]
}
Output:

10
The rod can be cut in the ways given below:

1 + 1 + 1 + 1 inches will cost price[0] + price[0] + price[0] + price[0] = 4
1 + 1 + 2 inches will cost price[0] + price[0] + price[1] = 7
1 + 3 inches will cost price[0] + price[2] = 9
2 + 2 inches will cost price[1] + price[1] = 10
One piece of 4 inches will cost price[3] = 9
The maximum profit is obtained by cutting it into two pieces 2 inches each.

Notes
Constraints:

1 <= n <= 103
1 <= price of any sized piece of the rod <= 105
"""


def get_maximum_profit(price):
    """
    Args:
     price(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    length = len(price)
    dp_list = [0] * (length + 1)

    for l in range(1, length + 1):
        for c in range(1, l+1):
            dp_list[l] = max(dp_list[l],
                             dp_list[l-c] + price[c-1])

    return dp_list[length]
