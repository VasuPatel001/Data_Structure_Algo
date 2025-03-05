"""
Word Break
IK Problem: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484806-923663-248-9483

Given a string and a dictionary of words, check whether the given string can be broken down into a space-separated sequence of one or more dictionary words.

Example One
{
"s": "helloworldhello",
"words_dictionary": ["world", "hello", "faang"]
}
Output:

1
helloworldhello can be broken down as hello world hello.

Example Two
{
"s": "interviewkickstart",
"words_dictionary": ["interview", "preparation"]
}
Output:

0
Notes
The same word in the dictionary may be used multiple times in the breakdown process.

Constraints:

1 <= length of given string <= 103
1 <= number of words in the dictionary <= 103
1 <= length of each word in the dictionary <= 20
Each string consists of lowercase English alphabets only.
All words in the dictionary are unique.
"""


def word_break(s, words_dictionary):
    """
    Args:
     s(str)
     words_dictionary(list_str)
    Returns:
     bool

    Time: O(n^2)
    Space: O(n)
    """
    # Write your code here.
    n = len(s)
    dp_list = [False for _ in range(n + 1)]
    dp_list[n] = True

    word_set = {word for word in words_dictionary}

    for i in range(n-1, -1, -1):
        word = ''
        for j in range(i, n, 1):
            word += s[j]

            if len(word) > 20:
                break

            if dp_list[j+1] and (word in word_set):
                dp_list[i] = True
                break

    return dp_list[0]
