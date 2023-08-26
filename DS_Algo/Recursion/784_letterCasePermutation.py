"""
Leetcode 784: Letter case permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:
1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""


class Solution:
    def helper(self, s, cur_idx, slate, result):
        if cur_idx == len(s):
            result.append("".join(slate))
            return

        # sub_problem != 0
        ch = s[cur_idx]
        if ch.isalpha():
            # lower case
            slate.append(ch.lower())
            self.helper(s, cur_idx + 1, slate, result)
            slate.pop()

            # upper case
            slate.append(ch.upper())
            self.helper(s, cur_idx + 1, slate, result)
            slate.pop()
        else:  # ch is a numeric digit
            slate.append(ch)
            self.helper(s, cur_idx + 1, slate, result)
            slate.pop()

    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        self.helper(s, 0, [], result)
        return result
