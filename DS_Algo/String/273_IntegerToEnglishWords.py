"""
Leetcode 273. Integer to English Words
Hard

Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
0 <= num <= 231 - 1
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
        words = []
        i = 0
        while num > 0:
            triplet = num % 1000
            num = num // 1000
            if triplet == 0:
                i += 1
                continue
            temp = []
            if triplet // 100 > 0:
                temp.append(ones[triplet // 100])
                temp.append("Hundred")
            if triplet % 100 >= 10 and triplet % 100 <= 19:
                temp.append(teens[triplet % 10])
            else:
                if triplet % 100 >= 20:
                    temp.append(tens[triplet % 100 // 10])
                if triplet % 10 > 0:
                    temp.append(ones[triplet % 10])
            if i > 0:
                temp.append(suffixes[i])

            words = temp + words
            i += 1
        return " ".join(words)
