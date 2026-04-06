class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers
        # placing:
        # opposite ends: 
        # beginning: if we get every area: O(n^2)
        
        # area = (min(left, right) * (rIndex - lIndex))
        # limiting factor is height, we track changes as they close in
        # width won't be a problem
        maxArea = 0
        left, right = 0, len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea