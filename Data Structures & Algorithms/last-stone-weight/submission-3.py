class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap = [-stone for stone in stones]
        heapq.heapify(self.max_heap)
        while len(self.max_heap) > 1:
            stone1 = -heapq.heappop(self.max_heap)
            stone2 = -heapq.heappop(self.max_heap)
            if (stone1 - stone2) > 0:
                heapq.heappush(self.max_heap, -(stone1 - stone2))
        return -self.max_heap[0] if self.max_heap else 0