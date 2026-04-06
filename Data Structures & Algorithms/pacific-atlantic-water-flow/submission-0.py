class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # explore from pacific,
        # explore from atlantic
        # if they can reach both locations, add in final list
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pac, atl = set(), set()
        row_len, col_len = len(heights), len(heights[0])
        res = []
        # otherwise dfs
        def dfs(r, c, seen, prevHeight):
            if (r < 0 or c < 0 or r >= row_len or c >= col_len
            or heights[r][c] < prevHeight or (r, c) in seen):
                return
            seen.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, seen, heights[r][c])
            
        for c in range(col_len):
            dfs(0, c, pac, heights[0][c])
            dfs(row_len - 1, c, atl, heights[row_len - 1][c])
        for r in range(row_len):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col_len - 1, atl, heights[r][col_len-1])

        for r in range(row_len):
            for c in range(col_len):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res