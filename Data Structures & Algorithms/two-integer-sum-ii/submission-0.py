class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, n in enumerate(numbers):
            complement = target - n
            if complement in dictionary:
                return [dictionary[complement]+1, i+1]
            dictionary[n] = i