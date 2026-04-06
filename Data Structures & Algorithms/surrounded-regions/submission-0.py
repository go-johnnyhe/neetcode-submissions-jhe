class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 4 directionally connected 0s

        '''
        dfs: keep going 4 directions of O, until it's on the border or no more,
             if we hit border, leave as is, else mark all the Os we saw to X
             
        '''
        if not board:
            return
        m, n = len(board), len(board[0])
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r, c, region, border_touch):
            if (r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "O" or (r, c) in visited):
                return
            
            visited.add((r, c))
            region.append((r, c))

            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                border_touch[0] = True

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr,nc, region, border_touch)
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r,c) not in visited:
                    region = []
                    border_touch = [False]

                    dfs(r,c,region,border_touch)

                    if not border_touch[0]:
                        for x, y in region:
                            board[x][y] = "X"