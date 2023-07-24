"""
Levenshtein Distance
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
The minimum number of steps required to convert word1 to word2 with the given set of allowed operations is called edit distance. e.g. Minimum edit distance between the words 'kitten' and 'sitting', is 3.

kitten → sitten (substitution of "s" for "k")
sitten → sittin (substitution of "i" for "e")
sittin → sitting (insertion of "g" at the end)
Read more about edit distance here.

Example One
{
"word1": "cat",
"word2": "bat"
}
Output:

1
Example Two
{
"word1": "qwe",
"word2": "q"
}
Output:

2
Notes
Constraints:

1 <= length of the strings word1 and word2 <= 105
word1 and word2 contains lower case alphabets from 'a' to 'z'.
"""


def levenshtein_distance(word1, word2):
    """
    Args:
     word1(str)
     word2(str)
    Returns:
     int32
    """
    # Write your code here.
    w1 = len(word1)
    w2 = len(word2)
    dp_table = [[0 for _ in range(w2+1)] for _ in range(w1+1)]

    # base case
    for col in range(w2+1):
        dp_table[w1][col] = w2 - col

    for row in range(w1+1):
        dp_table[row][w2] = w1 - row
    dp_table[w1][w2] = 0
    print(dp_table)
    for row in range(w1 -1, -1, -1):
        for col in range(w2 -1, -1, -1):
            count_replace = 0 if word1[row] == word2[col] else 1
            dp_table[row][col] = min(dp_table[row+1][col+1] + count_replace,
                                     dp_table[row][col+1] + 1,
                                     dp_table[row+1][col] + 1)

    print(dp_table)
    return dp_table[0][0]
