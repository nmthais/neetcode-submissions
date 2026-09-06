class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        totalProduct=1
        indexZero = -1
        if nums.count(0) == 1:
            indexZero = nums.index(0)
            nums[indexZero] = 1
        elif nums.count(0) > 1:
            indexZero = -2
        for i in nums :
            totalProduct *= i
        
        for index,value in enumerate(nums):
            if indexZero != -1:
                if index != indexZero:
                    res.append(totalProduct*0)
                else:
                    res.append(totalProduct)
            else:
                res.append(int(totalProduct/nums[index]))
            
        return res