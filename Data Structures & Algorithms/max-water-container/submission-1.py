class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr = 0
        currHighest=0
        i = 0
        j = len(heights) -1
        while i<j:
            curr = (j-i) * min(heights[i], heights[j])
            if (curr > currHighest):
                currHighest = curr
            if heights[i] > heights[j]:
                j-=1
            elif heights[i] <=heights[j]:
                i+=1
        return currHighest