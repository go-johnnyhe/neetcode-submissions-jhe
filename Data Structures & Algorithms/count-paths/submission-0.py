class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom and right all have one, anything else is built on that
        # wall roles all get 1. m, n == 1
        grid = [[0] * n for i in range(m)]
        for i in range(n):
            grid[m-1][i] = 1
        for i in range(m):
            grid[i][n - 1] = 1
        for r in range(len(grid) - 2, -1, -1):
            for c in range(len(grid[0]) - 2, -1, -1):
                grid[r][c] = grid[r][c+1] + grid[r+1][c]
        
        return grid[0][0]