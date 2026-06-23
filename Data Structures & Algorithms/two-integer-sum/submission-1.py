class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create map intended to track seen values and their indices.
        # key = value ; value = index
        seen_map = {}

        for i in range(len(nums)): #iterate through nums, one index at a time           
           complement = target - nums[i] # compute complement -- insight is if complement is in the map -- we have our indices.
           if complement in seen_map:
            return [seen_map[complement], i]
           seen_map[nums[i]] = i # add seen values index and its value to map
        

