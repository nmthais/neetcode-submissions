class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []  # monotonic increasing
        maxArea = 0
        for i in range(n+1):
            while stack and (i==n or heights[i] <= heights[stack[-1]]):
                h = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(h * width, maxArea)
            stack.append(i)
        
        return maxArea