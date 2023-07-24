"""
Word Break Count
Given a dictionary of words and a string txt, find the number of ways the string can be broken down into the dictionary words. Return the answer modulo 109 + 7.

Example
{
"dictionary": ["kick", "start", "kickstart", "is", "awe", "some", "awesome"],
"txt": "kickstartisawesome"
}
Output:

4
Here are all four ways to break down the string into the dictionary words:

kick start is awe some
kick start is awesome
kickstart is awe some
kickstart is awesome
4 % 1000000007 = 4 so the correct output is 4.

Notes
Constraints:

1 <= number of words in the dictionary <= 2 * 105
1 <= length of any dictionary word <= 102
1 <= length of the string txt <= 2 * 103
Dictionary words and the string txt all consist of lowercase latin characters only (no whitespace, in particular).
"""


def word_break_count(dictionary, txt):
    """
    Args:
     dictionary(list_str)
     txt(str)
    Returns:
     int32
    """
    # Write your code here.

    word_set = {word for word in dictionary}

    n = len(txt)
    dp_list = [-1 for _ in range(n+1)]
    MOD = 1000000007

    def solve(idx: int, word_set: set, txt: str, dp_list: list[int]):
        nonlocal n
        nonlocal MOD
        if idx == n:
            return 1

        if dp_list[idx] != -1:
            return dp_list[idx]

        # internal node worker
        result = 0
        segment = ''
        for i in range(idx, n):
            segment += txt[i]
            if segment in word_set:
                numOfArrangements = solve(i+1, word_set, txt, dp_list)
                result += numOfArrangements
                result %= MOD

        dp_list[idx] = result
        return dp_list[idx]

    return solve(0, word_set, txt, dp_list)
