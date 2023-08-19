"""
IK Problem: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484810-924784-63-376-4910715

Maximum In Sliding Window
Given an array of integers arr of size n and an integer w, find maximum number in all subarrays of arr of length w.

Imagine that n is very large and a sliding window of a smaller size w is moving through arr from left to right. We need to find the maximum in every position of the sliding window.

Example
{"arr": [1, 3, -1, -3, 5, 3, 6, 7],
"w": 3}
Output:
[3, 3, 5, 5, 6, 7]

Size of arr is 8 and so the size of the output array is n - w + 1 = 8 - 3 + 1 = 6.
Here are all the 6 positions of the sliding window and the corresponding maximum values:

[1 3 -1] -3 5 3 6 7. Maximum is 3.
1 [3 -1 -3] 5 3 6 7. Maximum is 3.
1 3 [-1 -3 5] 3 6 7. Maximum is 5.
1 3 -1 [-3 5 3] 6 7. Maximum is 5.
1 3 -1 -3 [5 3 6] 7. Maximum is 6.
1 3 -1 -3 5 [3 6 7]. Maximum is 7.

Notes
Function must return an array of integers of length n - w + 1. i-th value in the returned array must be the maximum among arr[i], arr[i + 1], ..., arr[i + w - 1].

Constraints:
1 <= n <= 105
-2 * 109 <= arr[i] <= 2 * 109
1 <= w <= n
"""
from collections import deque


def max_in_sliding_window(arr, w):
    """
    Args:
     arr(list_int32)
     w(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    """
    Asymptotic complexity in terms of size of `arr` `n` and `w`:
    Time: O(n)
    Auxiliary space: O(w)
    Total space: O(n)
    """
    n = len(arr)
    ans = [0] * (n - w + 1)
    indices = deque()  # deque keeps track of indcies & not the values

    for i in range(n):
        # pop any useless indices that are less than arr[i]
        while indices and arr[indices[-1]] <= arr[i]:
            indices.pop()

        # append current element's index to the end of the deque
        indices.append(i)

        # Next if condition makes sure we don't start filling up ans too early,
        # before we have processed w elements of arr.
        if i >= w - 1:
            # making sure there isn't an out-of-window element in the deque.
            # This is the reason why deque stores indices and not actual values
            if indices[0] <= (i - w):
                indices.popleft()

            # first element in the deque is the greatest of all, by design
            ans[i - w + 1] = arr[indices[0]]
    return ans
