class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        max_len = 0
        current_streak = 1
        for num in nums:
            if num-1 in nums_set: # this means num is not the start of a sequence, so ignore it.
                current_streak=1 # reset current_streak to 1.
            
            current_num = num
            while current_num+1 in nums_set:
                current_streak+=1
                current_num+=1
            
            max_len = max(max_len, current_streak)
            current_streak = 1
        
        return max_len