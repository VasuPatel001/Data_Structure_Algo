"""
Write a function that returns whether a list of strings is sorted given a specific alphabet.
A list of N words and the K-sized alphabet are given.

input:  words =    ["cat", "bat", "tab"]
        alphabet = ['c', 'b', 'a', 't']
output: True

["bot", "cat"] --> True
["hell", "hello" ] --> True
["hello", "hell" ] ---> False
"""
# Optimal Solution


def inOrder(word1, word2, alpha_dict) -> bool:
    for i in range(min(len(word1), len(word2))):
        if alpha_dict[word1[i]] < alpha_dict[word2[i]]:
            return True
        if alpha_dict[word1[i]] > alpha_dict[word2[i]]:
            return False
    return len(word1) < len(word2)


def check_words_alpha(words: list[str], alphabet: list[str]) -> bool:
    alpha_dict = {}
    for idx, alpha in enumerate(alphabet):
        alpha_dict[alpha] = idx
    for i in range(len(words)-1):
        if not inOrder(words[i], words[i+1], alpha_dict):
            return False
    return True


# Non-optimal solution
def check_words_alpha(words: list[str], alphabet: list[str]) -> bool:
    """
    Time: O(n*m) n words and m being the max character length
    Space: O(k+m)
    """
    i, j = 0, 1

    alpha_dict = {}
    # for idx, alpha in alphabet.items(): 
    for idx, alpha in enumerate(alphabet):  # O(k)
        alpha_dict[alpha] = idx

    while j <= len(words)-1:
        first = words[i]  # O(m)
        second = words[j]   # O(m)
        run_test = min(len(first), len(second))

        for test_idx in range(run_test):
            if alpha_dict[first[test_idx]] < alpha_dict[second[test_idx]]:
                break
            elif alpha_dict[first[test_idx]] == alpha_dict[second[test_idx]]:
                if test_idx == len(second) - 1 and test_idx < len(first) - 1:
                    return False
                else:
                    continue
            else:  # >
                return False

        i += 1
        j += 1

    return True
