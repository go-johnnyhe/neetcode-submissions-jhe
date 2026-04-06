import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # rank the points by their distance to the origin
        # create min heap and pop when its size > k
        # return the min heap
        max_heap = []
        for a, b in points:
            distance = -(a**2+b**2)
            heapq.heappush(max_heap, (distance, [a, b]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [point for _, point in max_heap]