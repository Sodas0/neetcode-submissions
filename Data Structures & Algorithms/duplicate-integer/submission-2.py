class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # HASH MAP
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                return True
        return False
        
