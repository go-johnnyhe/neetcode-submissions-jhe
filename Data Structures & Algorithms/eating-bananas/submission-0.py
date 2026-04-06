class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min: 1
        # max: largest num in the pile
        # get mid

        # say 12 for [25,10,23,4]
        # ceil(25/12) -> 3
        # ceil(0/12) -> 1
        # ceil(23/12) -> 2
        # -> 1
        # if sum hours < h:
        # max = mid - 1
        # elif > h:
        # min = mid + 1
        maximum = 0
        for num in piles:
            maximum = max(maximum, num)
        minimum = 1
        result = 1
        while minimum <= maximum:
            mid = (minimum + maximum) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if totalTime <= h:
                result = mid
                maximum = mid - 1
            else:
                minimum = mid + 1
        return result
                