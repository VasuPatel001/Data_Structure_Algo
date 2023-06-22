"""
https://uplevel.interviewkickstart.com/resource/rc-codingproblem-578599-921813-56-343

Find Order Of Characters In Alien Dictionary
Given a sorted dictionary of an alien language, find the order of characters in the alphabet.

Example One
{"words": ["baa", "abcd", "abca", "cab", "cad"]}
Output:
"bdac"

Example Two
{"words": ["caa", "aaa", "aab"]}
Output:
"cab"

Notes
Given dictionary is sorted in the lexicographical order of the alien language.
Output is a string consisting of all the characters of the alien alphabet, in order.

Constraints:
1 <= total length of all the words in the dictionary <= 105
Input will consist of lowercase latin characters only
Input will be such that it is possible to determine the alphabet order uniquely
The dictionary may contain duplicate words
"""


def find_order(words):
    """
    Args:
     words(list_str)
    Returns:
     str
    """
    # Write your code here.
    # Step 1: form a graph (adjacency list)
    n = len(words)

    adjDict = {}  # dict[str: list[str]]
    # IMP Step: initialize nodes with no-edges, 
    # otherwise test cases having only one type of character will fail.
    for i in range(n):
        for j in range(len(words[i])):
            adjDict[words[i][j]] = []

    # find mismatch and add edge
    for i in range(len(words)-1):
        min_len = min(len(words[i]), len(words[i+1]))
        for j in range(min_len):
            if words[i][j] != words[i+1][j]:
                adjDict[words[i][j]].append(words[i+1][j])
                break

    # array initialization for book-keeping of dfs topsort
    visited = {}  # dict(str: int)
    arrival = {}  # dict(str: int)
    departure = {}  # dict(str: int)
    timestamp = [0]
    topsort_ch = []  # list[str]

    # classical topsort code
    def dfs(node):
        visited[node] = 1
        arrival[node] = timestamp[0]
        timestamp[0] += 1

        for neighbor in adjDict[node]:
            if neighbor not in visited:
                visited[neighbor] = 1
                # parent[neighbor] = node
                dfs(neighbor)
            else:  # neigbor is already visited
                if departure[neighbor] == -1:
                    continue
        departure[node] = timestamp[0]
        timestamp[0] += 1
        topsort_ch.append(node)

    # outer loop: loop over unvisited nodes
    for node in adjDict.keys():
        if node not in visited:
            dfs(node)

    # reverse topsort order to obtain the characters in proper order for alien dictionary.
    topsort_ch.reverse()

    return ''.join(topsort_ch)