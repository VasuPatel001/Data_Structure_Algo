"""
Equal Subset Partition
IK coding problem: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484805-923140-57-349

Given an array s of n integers, partition it into two non-empty subsets, s1 and s2, such that the sum of all elements in s1 is equal to the sum of all elements in s2. Return a boolean array of size n where i-th element is 1 if i-th element of s belongs to s1 and 0 if it belongs to s2.

Example
{
"s": [10, -3, 7, 2, 1, 3]
}
Output:

[1, 1, 0, 0, 0, 1]
There are multiple partitionings where s1 sums up to 10 and s2 sums up to 10; they are all correct answers:

s1 = [ 10 , -3 , 3 ] and s2 = [ 7 , 2 , 1 ] (Sample output)

s1 = [ 7 , 2 , 1 ] and s2 = [ 10 , -3 , 3 ]

s1 = [10] and s2 = [-3, 3, 7, 2, 1]

s1 = [-3, 3, 7, 2, 1] and s2 = [10]

s1 = [10, -3, 2, 1] and s2 = [7, 3]

s1 = [7, 3] and s2 = [10, -3, 2, 1].

Notes
Any valid answer will be accepted.
If such partitioning is not possible, return an empty array.
Constraints:

1 <= n <= 100
-100 <= elements in s <= 100
"""


def equal_subset_sum_partition(s):
    """
    Args:
     s(list_int32)
    Returns:
     list_bool
    """
    # Write your code here.
    # Store min and max sum possible for given array.
    sum_neg = 0
    sum_pos = 0
    for val in s:
        if val < 0:
            sum_neg += val
        else:
            sum_pos += val

    # Total sum of the array.
    total_sum = sum_pos + sum_neg
    # Partition not possible.
    if total_sum % 2 != 0:
        return []

    n = len(s)

    # dp state
    dp = [{} for _ in range(n)]

    # Base state:
    # for idx 0 only one sum s[0] is possible
    dp[0][s[0]] = True

    for i in range(1, n):
        # Iterate on all possible subset sum.
        for val in range(sum_neg, sum_pos + 1):
            # dp state-transition:

            # 1) state(i, val) = state(i - 1, val) without taking current element.
            dp[i][val] = dp[i - 1].get(val, False)

            # 2) if val == s[i], just taking i-th element is sufficient.
            if val == s[i]:
                dp[i][val] = True
            elif val - s[i] >= sum_neg:
                # 3) state(i, val) = state(i - 1, val - s[i]) when taking current element.
                dp[i][val] |= dp[i - 1].get(val - s[i], False)

    required = total_sum // 2
    idx = n - 1

    # Parition not possible.
    if not dp[idx].get(required, False):
        return []

    # Tracks partition elements.
    result_subset = [False] * len(s)
    # Tracks count of elements included in S1.
    cnt = 0
    while idx >= 0:
        if idx != 0:
            # Reverse dp transition.
            if dp[idx].get(required, False) and not dp[idx - 1].get(required, False):
                result_subset[idx] = True
                cnt += 1
                required -= s[idx]
                if required == 0:
                    break
        else:
            result_subset[idx] = True
            cnt += 1
        idx -= 1

    # Checks whether all elements are included in S1.
    # All elements will be in S1 if total_sum = 0
    # case when s = [-2, 2]
    # partition is not possible in this case.
    if cnt == n:
        result_subset = []

    return result_subset
