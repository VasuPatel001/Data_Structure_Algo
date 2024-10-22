def maxPathSum(grid: list[list[int]]):
    """
    Time: O(mn)
    Space: O(mn)
    """
    m = len(grid)
    n = len(grid[0])
    table = [[0 for _ in range(n)] for _ in range(m)]

    table[0][0] = grid[0][0]

    for col in range(1, n):
        table[0][col] = table[0][col-1] + grid[0][col]

    for row in range(1, m):
        table[row][0] = table[row-1][0] + grid[row][0]
    
    for row in range(1, m):
        for col in range(1, n):
            table[row][col] = grid[row][col] + max(table[row-1][col], table[row][col-1])
    
    return table[m-1][n-1]