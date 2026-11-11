class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        #first pass: prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # store
            prefix *= nums[i] # update
        
        # second pass: suffix
        suffix = 1
        for i in range(len(nums)-1, -1, -1): #right to left
            res[i] *= suffix
            suffix *= nums[i]
        return res