class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # maintain a min heap of length k, so we can conveniently pop
        # the least frequent anytime
        # dictionary to track frequency, and put in it and the 
        # corresponding number
        heap = []
        freq = Counter(nums)

        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res