class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res : List[List[int]] = []
        if len(nums) <3:
            return res
        elif len(nums) == 3:
            if (nums[0] + nums[1] + nums[2]) != 0:
                return res
            else:
                res.append([nums[0], nums[1], nums[2]])
                return res
        else:
            nums.sort()
            for index in range(len(nums)):
                curr = 0 - nums[index]
                j = index + 1
                k = len(nums) -1
                while j < k:
                    if nums[j] + nums[k] == abs(curr) and not ([nums[index], nums[j], nums[k]] in res):
                        res.append([nums[index], nums[j], nums[k]])
                        j+=1
                        k-=1 
                    elif nums[j] + nums[k] < abs(curr):
                        j+=1
                    else:
                        k-=1
                       
        return res

