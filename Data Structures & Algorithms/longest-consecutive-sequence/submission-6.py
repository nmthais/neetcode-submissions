class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        curr = 1
        currHighest = 1
        print(sorted(nums))
        numSorted = sorted(nums)
        for index in range(len(numSorted)-1):
            if numSorted[index + 1] == numSorted[index]:
                continue
            if numSorted[index + 1] == numSorted[index] + 1:
                curr +=1
            else:
                curr=1
            if curr > currHighest:
                currHighest = curr
        return currHighest

    