import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a dictionary of frequencies

        # loop k, get the max value, append to result arr, take it out

        counter = Counter(nums)
        
        return heapq.nlargest(k, counter.keys(), key=counter.get)
