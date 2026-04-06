class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # traverse each spot, when you see an island --> dfs & count max area
        # remember each spot
        
        maxArea = 0
        seen = set()
        def dfs(r, c):
            if (r, c) in seen or grid[r][c] == 0 or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0
            seen.add((r,c))
            area = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    area += dfs(nr, nc)
            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == 1:
                    maxArea = max(dfs(r, c), maxArea)
        return maxArea