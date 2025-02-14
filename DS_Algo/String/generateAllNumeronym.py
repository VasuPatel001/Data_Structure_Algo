"""
IK: Generate All Numeronyms
https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484815-924793-66-398-7866480

Given a word, generate all possible numeronyms for it.

What is a numeronym?

A numeronym is a word where a number is used to form an abbreviation.

A numeronym for a word is another word with two or more contiguous letters replaced with their number. Exactly one set of contiguous letters is replaced by a number. First or last letter in the initial word are never omitted/replaced when forming a numeronym for it.

Example
{
"word": "nailed"
}
Output:

["n4d", "na3d", "n3ed", "n2led", "na2ed", "nai2d"]
"n4d" is an abbreviation of "nailed" where substring "aile" is replaced by the number of letters in it, 4.

"na3d" is an abbreviation of "nailed" where substring "ile"is replaced by number of letters in it, 3.

And so on.

Notes
Order of strings in the output is not important.
If no numeronyms can be generated for the word, return an empty list.
Constraints:

Possible characters in the word: [a-z] and [A-Z]
1 <= length of the word <= 120
"""

def generate_all_numeronyms(word):
    """
    Args:
     word(str)
    Returns:
     list_str
    """
    """
    For any given string str, length of omitted characters l can be 2 <= l <= n - 2 where n is length of string as we can’t omit first and last characters and we need to find a numeronym in which at least 2 contiguous letters were omitted.

    So for any given length l, we iterate over all possible positions from where omission of characters can start, find a string of length l from that position and replace that with l (number of omitted characters).

    Time Complexity
    O(n3).
    As iteration will be in three loops, first over possible lengths then over possible first characters of omitted characters and then to find store newly created numeronym.

    Auxiliary Space Used
    O(n3).
    Maximum number of possible numeronyms generated can be O(n2) and length of each will be O(n) hence it takes O(n3) to store output.

    Space Complexity
    O(n3).
    It will be equal to auxiliary space as in input we are just reading a single input string of length n which takes O(n). O(n3) + O(n) = O(n3)
    """
    # Write your code here.
    n = len(word)
    if n <= 3:
        return []

    result = []

    for length in range(2, n-1, 1):
        tmp = ""
        for start_idx in range(1, n-length, 1):
            tmp = word[:start_idx] + str(length) + word[start_idx+length:]
            result.append(tmp)

    return result
