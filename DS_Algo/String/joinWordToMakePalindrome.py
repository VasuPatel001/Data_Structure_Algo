"""
IK Join Words To Make A Palindrome
https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484815-924793-66-396-7866480

Given a list of strings words, of size n, check if there is any pair of words that can be joined (in any order) to form a palindrome then return the pair of words forming palindrome.

Example One
{
"words": ["bat", "tab", "zebra"]
}
Output:

["bat", "tab"]
As "bat" + "tab" = "battab", which is a palindrome.

Example Two
{
"words": ["ant", "dog", "monkey"]
}
Output:

["NOTFOUND", "DNUOFTON"]
As for each 6 combinations of string of words, there is no single generated word which is a palindrome hence result list will be ["NOTFOUND", "DNUOFTON"].

Notes
If there are multiple correct answers, return any one.
In case of no answer return list ["NOTFOUND", "DNUOFTON"].
Constraints:

1 <= length of a word <= 30
2 <= n <= 20000
Words consist of characters ['a'-'z'], ['A'-'Z'], ['0'-'9']
"""


def join_words_to_make_a_palindrome(words):
    """
    Args:
     words(list_str)
    Returns:
     list_str
    """
    # # Write your code here.
    """
    Time Complexity
    O(n2 * l).
    As there are total 2 * nC2 ordered pair of words, and for each pair, for finding whether that pair is forming palindrome or not will take O(l). So, time complexity of this solution will be O(n2 * l).

    Auxiliary Space Used
    O(l).
    As we are storing result list of two words of maximum length l.

    Space Complexity
    O(n * l).
    Input will take space O(n * l) because we are storing n words of list words where maximum possible length of word can be l and auxiliary space used is O(l). So, O(n * l) + O(l) = O(n * l).
    """
    # from itertools import combinations
    # pairs = combinations(words, 2)
    # result = []
    # for pair in pairs:
    #     test_str = pair[0] + pair[1]
    #     if test_str == test_str[::-1]:
    #         return [pair[0], pair[1]]
    # return ["NOTFOUND", "DNUOFTON"]
    
    """
    A better approach would be as follows from some observations:
    Let's say there exists a pair of words (words[x], words[y]), such that result = words[x] + words[y] is a palindrome.

    Two cases are possible here:
    CASE 1: words[x].length() >= words[y].length()
    Iterating over words, considering the word in the current iteration as xth word in words. Task is to find out if there exists some yth word, such that words[x] + words[y] is a palindrome. Now, if such y exists, it must be of the form stringReverse(words[x].substring(0, k)), for some 0 <= k < words[x].length().

    So, now we only need to find such k, such that words[y] == stringReverse(words[x].substring(0, k)) and words[x].substring(k + 1, words[x].length()) is a palindrome, if k + 1 < words[x].length().

    CASE 2: words[x].length() < words[y].length()
    Iterating over words, considering the word in the current iteration as xth word in words. Task is to find out if there exists some yth word, such that words[y] + words[x] is a palindrome. Now, if such y exists, it must be of the form stringReverse(words[x].substring(k, words[x].length())), for some 0 <= k < words[x].length().

    So, now we only need to find such k, such that words[y] == stringReverse(words[x].substring(k, words[x].length())) and words[x].substring(0, k) is a palindrome, if (k > 0).

    Both cases require a quick lookup of words in list words. So, we can use hashset or hashMap here for constant time (amortized time) lookup of words. Also, in some cases, for eg. "aaaaa", we need to know the frequency of words so that same word (same indexed word in list of words) doesn't get picked up as another word to make a palindrome. So, a hashmap having word as key and frequency of that word as value will work here. See the implementation for better understanding.

    Time Complexity
    O(n * l2).
    As while iterating over list of words, considering the word in current iteration as left_word, we have to do two lookups and two palindrome check for each k, 0 <= k < length(left_word), time complexity will be O(l2) for each word left_word.
    So, total time complexity will be O(n * l2).

    Auxiliary Space Used
    O(n * l).
    As we are maintaining a hashmap of frequencies of words for n words of list words, space complexity to maintain this will be O(n * l) and we are storing result list of two words of maximum length l.
    O(n * l) + O(l) = O(n * l).

    Space Complexity
    O(n * l).
    Input will take space O(n * l) because we are storing n words of list words where maximum possible length of word can be l and auxiliary space used is O(n * l). So, O(n * l) + O(n * l) = O(n * l).
    """
    from collections import Counter
    result = ["NOTFOUND", "DNUOFTON"]
    count = Counter(words)

    for left_word in words:
        current = ""

        # CASE 1: words[x] + words[y] is a palindrome
        for j in range(len(left_word)):
            current = left_word[j] + current
            if current in count:
                if current == left_word:
                    if count[current] > 1:
                        return [left_word, current]
                elif is_palindrome(left_word[j + 1:]):
                    return [left_word, current]

        current = ""

        # CASE 2: words[y] + words[x] is a palindrome
        for j in range(len(left_word) - 1, -1, -1):
            current = current + left_word[j]
            if current in count:
                if current == left_word:
                    if count[current] > 1:
                        return [current, left_word]
                elif is_palindrome(left_word[:j]):
                    return [current, left_word]

    return result


def is_palindrome(s):
    return s == s[::-1]
