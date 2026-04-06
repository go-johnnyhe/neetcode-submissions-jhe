class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # maintain a min heap of length k, so we can conveniently pop
        # the least frequent anytime
        # dictionary to track frequency, and put in it and the 
        # corresponding number
        heap = []
        freq = Counter(nums)

        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res