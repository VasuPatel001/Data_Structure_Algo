"""
Leetcode 79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Intuition
        The problem can be solved by traversing the grid and performing a depth-first search (DFS) 
        for each possible starting position. At each cell, we check if the current character matches 
        the corresponding character of the word. If it does, we explore all four directions (up, down, left, right) 
        recursively until we find the complete word or exhaust all possibilities.

        Time complexity:
        O(mXnX4^l), where m and n are the dimensions of the grid and l is the length of the word. The 4^l
        factor represents the maximum number of recursive calls we may have to make for each starting cell.

        Space complexity:
        O(l), where l is the length of the word. The space complexity is primarily due to the recursive stack 
        depth during the DFS traversal.
        """
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = ''

            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
