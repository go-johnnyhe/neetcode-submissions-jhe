class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # level by level traversal
        # initial sweep: add all rotten to queue
        #                count all fresh fruit ==> by the end check 0
    
        queue = deque()
        fresh_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minutes = 0
        while queue and fresh_count > 0:
            length = len(queue)
            minutes += 1
            for i in range(length):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
        if fresh_count != 0:
            return -1
        else:
            return minutes