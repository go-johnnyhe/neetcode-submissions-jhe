class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # explore one by one, skip water, check bounds, check if seen
        # when sees an island, counter +1
        # dfs goes up down left right
        seen = set()
        count = 0

        def dfs(r, c, seen, grid):
            if (r, c) in seen or grid[r][c] == "0":
                return
            seen.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for ar, ac in directions:
                nr, nc = r + ar, c + ac
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    dfs(nr, nc, seen, grid)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == "1":
                    count += 1
                    dfs(r, c, seen, grid)
                
        return count