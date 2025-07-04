class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 if [nums[i], nums[j], nums[k]] not in res:
        #                     res.append([nums[i], nums[j], nums[k]])
        # return res
        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l , r = i + 1 , len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([a , nums[l] , nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        

        return res



