class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n

        # first pass- compute prefix
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix*=nums[i]
    
        # second pass - we need to iterate backwards
        suffix = 1
        for i in range(n-1,-1,-1): #start,stop,step; stop is -1 because its not inclusive, meaning it stops at 0.
            out[i] *= suffix
            suffix*=nums[i]
        
        return out

