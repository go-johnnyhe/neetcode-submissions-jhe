class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # use dijkstra, but we track max val and curr position
        n = len(grid)
        m = len(grid[0])
        seen = set()
        pq = [(grid[0][0], 0, 0)]

        while pq:
            max_water, r, c = heapq.heappop(pq)
            if (r, c) == (n-1, m-1):
                return max_water
            
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in seen:
                    new_max_water = max(max_water, grid[nr][nc])
                    seen.add((nr, nc))
                    heapq.heappush(pq, (new_max_water, nr, nc))