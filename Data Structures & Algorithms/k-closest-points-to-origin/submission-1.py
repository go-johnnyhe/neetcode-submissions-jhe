class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.min_heap = []
        heapq.heapify(self.min_heap)
        res = []
        for a, b in points:
            distance = a**2 + b**2
            heapq.heappush(self.min_heap, (distance, [a, b]))
        for i in range(k):
            _, point = heapq.heappop(self.min_heap)
            res.append(point)
        return res