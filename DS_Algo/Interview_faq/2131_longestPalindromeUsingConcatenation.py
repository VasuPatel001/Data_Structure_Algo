"""
Leetcode 2131. Longest Palindrome by Concatenating Two Letter Words
Medium

You are given an array of strings words. Each element of words consists of two lowercase English letters.
Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
A palindrome is a string that reads the same forward and backward.

Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

Constraints:
1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
"""
from itertools import combinations
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairs = combinations(words, 2)
        singles = set()
        doubles = set()
        for word in words:  # time: O(n)
            if word[0] == word[1]:
                singles.add(word)

        for pair in pairs:  # time: O(nC2)
            if pair[0] == pair[1][::-1]:
                doubles.add(pair[0])
                doubles.add(pair[1])

        d = len(doubles)
        s = len(singles)
        h = 0
        if s > 0:
            h = d*2 + 2
        return max(d*2, 2, h)
