"""
IK code: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484815-924793-66-1602-7866480

Zigzag A Word
A word can be written in a vertical zigzag fashion in a given number of lines, e.g. KICKSTART in three lines looks like this:

K     S    T
I  K  T  R
C     A
Reading this text line by line gives us KSTIKTRCA.

Given a word and a number of lines for zigzagging, return that line-by-line representation.

Example One
{
"nlines": 4,
"word": "INTERVIEW"
}
Output:

"IINVETRWE"
Because zigzagging INTERVIEW in four lines gives this:

I        I
N     V  E
T  R     W
E
Example Two
{
"nlines": 1,
"word": "KICKSTART"
}
Output:

"KICKSTART"
Notes
Constraints:

1 <= word length <= 100000
1 <= number of lines <= 100000
Word consists of characters a..z, A..Z, 0..9
"""


def zigzag(nlines, word):
    """
    Args:
     nlines(int32)
     word(str)
    Returns:
     str
    """
    """
    Asymptotic complexity in terms `nlines` and length of `word`:
    Time: O(length of word).
    Auxiliary space: O(nlines + length of word).
    Total space: O(nlines + length of word).
    """
    if nlines == 1:
        return word

    length = len(word)
    lines = [""] * min(length, nlines)  # List to store content of each row.

    current_line = 0
    going_down = False
    word_index = 0

    while word_index < length:
        lines[current_line] += word[word_index]
        word_index += 1

        # Reverse direction at the topmost or bottommost row.
        if current_line == 0 or current_line == nlines - 1:
            going_down = not going_down

        current_line += 1 if going_down else -1

    return "".join(lines)
