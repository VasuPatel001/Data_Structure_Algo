"""
Leetcode 17: Letter combination of phone number
IK problem: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484787-905346-244-1535

Words From Phone Number
Given a seven-digit phone number, return all the character combinations that can be generated according to the following mapping:


Return the combinations in the lexicographical order.

Example One
{"phone_number": "1234567"}

Output:
[
"adgjmp",
"adgjmq",
"adgjmr",
"adgjms",
"adgjnp",
...
"cfilns",
"cfilop",
"cfiloq",
"cfilor",
"cfilos"
]
First string "adgjmp" in the first line comes from the first characters mapped to digits 2, 3, 4, 5, 6 and 7 respectively. Since digit 1 maps to nothing, nothing is appended before 'a'. Similarly, the fifth string "adgjnp" generated from first characters of 2, 3, 4, 5 second character of 6 and first character of 7. All combinations generated in such a way must be returned in the lexicographical order.

Example Two
{
"phone_number": "1234567"
}
Output:

[""]

Notes
Return an array of the generated string combinations in the lexicographical order. If nothing can be generated, return a list with an empty string "".
Digits 0 and 1 map to nothing. Other digits map to either three or four different characters each.

Constraints:
Input string is 7 characters long; each character is a digit.
"""


def helper(digits: str, cur_idx: int, slate: list[str], result: list[str], hmap: dict):
    if cur_idx == len(digits):
        if len(slate) > 0:
            result.append(''.join(slate))
        return
    
    # internal node worker
    for choice in hmap[digits[cur_idx]]:
        slate.append(choice)
        helper(digits, cur_idx + 1, slate, result, hmap)
        slate.pop()


def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    # Write your code here.
    hmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
    result = []
    phone_number = phone_number.replace('1', '')
    digits = phone_number.replace('0', '')
    if len(digits) == 0:
        return [""]
    helper(digits, 0, [], result, hmap)
    return result
