"""
IK: Longest Substring With Exactly Two Distinct Characters
https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484815-924793-66-395-7866480

Given a string s of length n, find the length of the longest substring that contains exactly two distinct characters.

Example
{
"s": "ecebaaaaca"
}
Output:

6
"aaaaca" is the largest substring with exactly 2 distinct characters.

Notes
If there are no such substrings, return 0.
Constraints:

1 <= n <= 105
s may contain English letters and digits.
"""

def get_longest_substring_length_with_exactly_two_distinct_chars(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    # Write your code here.
    """
    Optimal Solution
    * Asymptotic complexity in terms of size of `s` `n`:
    * Time: O(n).
    * Auxiliary space: O(1).
    * Total space: O(n).
    """
    from collections import defaultdict

    count_map = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        count_map[s[right]] += 1

        while len(count_map) > 2:
            count_map[s[left]] -= 1
            if count_map[s[left]] == 0:
                del count_map[s[left]]
            left += 1

        if len(count_map) == 2:
            max_len = max(max_len, right - left + 1)

    return max_len

    """
    Brute Fore Method:
    * Asymptotic complexity in terms of size of `s` `n`:
    * Time: O(n^2).
    * Auxiliary space: O(1).
    * Total space: O(n).
    """
    # longest_so_far = 0
    # n_unique_char = 0
    # for idx in range(len(s)):
    #     sub_str = ""
    #     for inner_idx in range(idx, len(s), 1):
    #         sub_str += s[inner_idx]
    #         if len(set(sub_str)) > 2:
    #             break
    #         if len(sub_str) > longest_so_far:
    #             longest_so_far = len(sub_str)
    # return longest_so_far
