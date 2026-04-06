class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                start = index
                maxArea = max(maxArea, (i - index) * height)
            stack.append((start, heights[i]))
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea