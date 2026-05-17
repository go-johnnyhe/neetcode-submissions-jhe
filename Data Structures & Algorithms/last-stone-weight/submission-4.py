class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        # -2 -2 -3 -4 -6
        while len(max_heap) > 1:
            # 6 4
            largest = heapq.heappop(max_heap) * -1
            second_largest = heapq.heappop(max_heap) * -1

            if largest > second_largest:
                heapq.heappush(max_heap, (largest - second_largest) * -1)

        if len(max_heap) == 1:
            return max_heap[0] * -1
        else:
            return 0
            
