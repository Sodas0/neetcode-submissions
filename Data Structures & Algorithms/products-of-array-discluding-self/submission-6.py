class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix; need 2 passes
        res = [1]*len(nums)

        # 1st pass:
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
        