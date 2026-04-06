class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowSet[r] or
                    board[r][c] in colSet[c] or
                    board[r][c] in squareSet[r//3,c//3]):
                    return False
                colSet[c].add(board[r][c])
                rowSet[r].add(board[r][c])
                squareSet[r//3, c//3].add(board[r][c])
        return True