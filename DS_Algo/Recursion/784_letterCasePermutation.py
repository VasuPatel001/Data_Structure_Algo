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
    """
    Solution with Mutable parameter
    Time Complexity:
        Leaf node worker: O(2^n * n)
        Internal node worker: O(2^n * n)
        Hence, total is O(2^n * n)
    Space Complexity:
        Input: O(n)
        Aux: O(n)
        Output: O(2^n * n)
    """
    def helper(self, s: str, cur_idx: int, slate: list[str]):
        # Base case/Leaf node worker
        if cur_idx == len(s):
            self.result.append("".join(slate))
            return

        # Internal node worker, sub_problem != 0
        ch = s[cur_idx]
        if ch.isalpha():
            # lower case
            slate.append(ch.lower())
            self.helper(s, cur_idx + 1, slate)
            slate.pop()

            # upper case
            slate.append(ch.upper())
            self.helper(s, cur_idx + 1, slate)
            slate.pop()
        else:  # ch is a numeric digit
            slate.append(ch)
            self.helper(s, cur_idx + 1, slate)
            slate.pop()

    def letterCasePermutation(self, s: str) -> list[str]:
        self.result = []
        self.helper(s, 0, [])
        return self.result
    
    ###########################################################################
    """
    Solution with OPTIMIZED Mutable parameter
    NOTE: Here we convert input string 's' to list[str], so as we can change
    the character in the list to upper/lower without creating slate [].

    Time Complexity:
        Leaf node worker: O(2^n * n)
        Internal node worker: O(2^n * n)
        Hence, total is O(2^n * n)
    Space Complexity:
        Input: O(n)
        Aux: O(n)
        Output: O(2^n * n)
    """
    def helper(self, s: list[str], cur_idx: int):
        # Base case/Leaf node worker
        if cur_idx == len(s):
            self.result.append("".join(s))
            return

        # Internal node worker, sub_problem != 0
        ch = s[cur_idx]
        if ch.isalpha():
            # lower case
            s[cur_idx] = s[cur_idx].lower()
            self.helper(s, cur_idx + 1)

            # upper case
            s[cur_idx] = s[cur_idx].upper()
            self.helper(s, cur_idx + 1)

        else:  # ch is a numeric digit
            self.helper(s, cur_idx + 1)

    def letterCasePermutation(self, s: str) -> list[str]:
        self.result = []
        self.helper(list(s), 0)
        return self.result

    ###########################################################################
    """
    Solution with IM-Mutable parameter
    NOTE: Here we use string concatenation which under the hood creates a new string

    Time Complexity:
        Leaf node worker: O(2^n * n)
        Internal node worker: O(2^n * n)
        Hence, total is O(2^n * n)
    Space Complexity:
        Input: O(n)
        Aux: O(n^2) NOTE: when using immuatable parameter, it leads to increase aux space usage.
        Output: O(2^n * n)
    """
    def helper(self, s: str, cur_idx: int, slate: str):
        # Base case/Leaf node worker
        if cur_idx == len(s):
            self.result.append(slate)
            return

        # Internal node worker, sub_problem != 0
        ch = s[cur_idx]
        if ch.isalpha():
            # lower case
            self.helper(s, cur_idx + 1, slate + ch.lower())

            # upper case
            self.helper(s, cur_idx + 1, slate + ch.upper())

        else:  # ch is a numeric digit
            self.helper(s, cur_idx + 1, slate + ch)

    def letterCasePermutation(self, s: str) -> list[str]:
        self.result = []
        self.helper(s, 0, "")
        return self.result
