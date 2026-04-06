class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for each island, we want to explore each point's up down left right
        # if it can go, we'll add count, otherwise if out of bounds
        # or water or seen before, we should stop traversing
        row, col = len(grid), len(grid[0])
        count = 0
        seen = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c, seen):
            if r < 0 or c < 0 or r == row or c == col or grid[r][c] == "0" or (r, c) in seen:
                return
            seen.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, seen)

        for r in range(row):
            for c in range(col):
                if (r, c) not in seen and grid[r][c] == "1":
                    count += 1
                    dfs(r, c, seen)
                # if I check here, definitely overcount since this increments on every point

        return count