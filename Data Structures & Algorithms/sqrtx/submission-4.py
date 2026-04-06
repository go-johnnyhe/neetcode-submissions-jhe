class Solution:
    def mySqrt(self, x: int) -> int:
        # l, r = 1, 13
        # mid == 7
        # 1 6
        # 
        # mid == 3
        # 4 6
        # mid == 5
        # 4 5
        # 
        # mid == 2
        # 
        l, r = 1, x
        res = 0
        while l <= r:
            mid = (l + r) // 2
            val = mid * mid
            if x == val:
                return mid
            elif val < x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res