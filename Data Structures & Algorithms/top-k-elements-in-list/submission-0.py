class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a dictionary of frequencies

        # loop k, get the max value, append to result arr, take it out

        dictionary = {}

        for num in nums:
            if num not in dictionary:
                dictionary[num] = 0
            else:
                dictionary[num] += 1
        
        result = []

        for i in range(k):
            maximum = max(zip(dictionary.values(), dictionary.keys()))[1]
            result.append(maximum)
            del dictionary[maximum]
        return result