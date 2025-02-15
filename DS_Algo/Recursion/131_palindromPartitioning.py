"""
Leetcode 131: Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]] 

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        self.result = []
        self.helper(s, 0, [])
        return self.result

    def helper(self, s: str, cur_idx: int, slate: list[str]):
        # back tracking case
        if len(slate) > 0 and not self.isPalindrome(slate[-1]):
            return

        # base case
        if cur_idx == len(s):
            self.result.append(slate[:])
            return

        # recursive case
        for pick in range(cur_idx, len(s)):
            slate.append(s[cur_idx:pick+1])
            self.helper(s, pick+1, slate)
            slate.pop()

    def isPalindrome(self, slate: str):
        return slate == slate[::-1]


if __name__ == "__main__":
    solve = Solution()
    s = "aab"
    print(solve.partition(s))
