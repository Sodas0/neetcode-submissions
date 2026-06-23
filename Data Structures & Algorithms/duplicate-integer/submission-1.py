class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hash map to track frequency, and if any element already exists in hashmap, return False
        frequency = {}
        for i in range(len(nums)): # iterate through every element in nums
            if nums[i] in frequency: # if the element is already in the hash map
                return True # we know it contains duplicate
                
            else: # if it is not in the hash map
                frequency[nums[i]] = 1 # add it to the hashmap
                continue 
        return False #after iterating everything and no duplciaate, must be no duplicates so return false

