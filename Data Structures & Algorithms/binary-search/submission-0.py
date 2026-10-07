class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        curr = 0
        left,right = 0, n-1
        while left <= right:
            curr = left + (right - left) //2
            if nums[curr] == target:
                return curr
            elif nums[curr] < target:
                left = curr + 1
            else:
                right = curr - 1 
        return -1