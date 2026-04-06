class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # l … r are *possible* starting indices of the k‑length window
        n = len(arr)
        l, r = 0, n - k

        while l <= r:
            m = (l + r) // 2

            # distance to the left border
            left = abs(x - arr[m])

            # distance to the right border — treat "past the end" as +∞
            right = abs(x - arr[m + k]) if m + k < n else math.inf

            if left > right:
                l = m + 1               # shift right
            else:
                r = m - 1  
        # after the loop `l` is the smallest index whose window wins
        return arr[l:l + k]