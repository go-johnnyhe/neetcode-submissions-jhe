class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # 0 1 2 3 4 5 6 7 8 9 10
        # . .     .     .
        stats = list(zip(position, speed))
        stats.sort(reverse=True)
        maxTime = 0
        fleets = 0
        for d, v in stats:
            t = (target - d) / v
            if t > maxTime:
                fleets += 1
                maxTime = t
        return fleets