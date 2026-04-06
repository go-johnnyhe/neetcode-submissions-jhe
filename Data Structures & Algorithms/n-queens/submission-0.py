class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # a series of decisions -> backtracking
        # [[. . . .]]
        # [[. . . .]]
        # [[. . . .]]
        # [[. . . .]]

        # if in same row, col, posDiag, negDiag sets, keep going,
        # else
            # add into their sets
            # keep going till n = 4, then 
            #      add to result array
            #      backtrack to the next one
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        backtrack(0)
        return res
        
