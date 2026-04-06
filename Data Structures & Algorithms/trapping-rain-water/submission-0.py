class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers: left & right
        # area: min(left & right) - bar height
        # l&r opposite we take whichever side is shorter
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]
        area = 0
        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                area += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                area += maxR - height[right]
        return area


