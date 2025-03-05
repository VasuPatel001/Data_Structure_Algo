"""
Leetcode 140. Word Break II
Hard

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        """
        Time Complexity:
            The time complexity of this solution is O(N² + 2ᴺ) in the worst case, where N is the length of the string s. Here's why:

            Recursive Calls:
            The function explores all possible segmentations, leading to O(2ᴺ) recursive calls in the worst case.
            This happens when each prefix of s is a valid word (e.g., "aaaaa" with ["a", "aa", "aaa", "aaaa"]).

            Substring Lookups:
            The function checks substrings of s (up to O(N²) in total) to find valid words.

            Memoization Reduces Redundant Computation:
            The memoization helps by preventing redundant calls for the same index.
            In practice, this significantly reduces the exponential calls, but the worst case remains exponential.

        Space Complexity:
            The space complexity is O(N² + 2ᴺ):

            Memoization Storage (O(N²)):

            The memo dictionary stores results for O(N) indices, each holding a list of sentences (each sentence could have O(N) words).
            Recursive Call Stack (O(N)):

            The recursion depth is at most O(N).
            Output Storage (O(2ᴺ)):

            In the worst case, the output can have O(2ᴺ) sentences, each consuming space.
        """
        word_set = set(wordDict)
        memo = {}

        def backtrack(index):
            if index in memo:
                return memo[index]

            if index == len(s):
                return [""]  # Base case: return empty string to help in constructing sentences

            sentences = []
            word = ""

            for j in range(index, len(s)):
                word += s[j]
                if word in word_set:
                    rest_sentences = backtrack(j + 1)
                    for sentence in rest_sentences:
                        sentences.append(word + (" " + sentence if sentence else ""))

            memo[index] = sentences
            return sentences

        return backtrack(0)
