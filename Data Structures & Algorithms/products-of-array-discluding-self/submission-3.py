class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n

        # first pass, compute prefix
        prefix = 1
        for i in range(n):
            answer[i]=prefix
            prefix*=nums[i]
        
        # second pass, compute suffix
        suffix = 1
        for i in range(n-1,-1,-1): # start at the last element, go backwards until the 0th element, stepping -1 each time.
            answer[i]*=suffix
            suffix*=nums[i]
        
        return answer