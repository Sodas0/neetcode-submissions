class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = {}
        highest_threshold = len(nums)//2 # floor 
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
            if freq_map[num]> highest_threshold:
                return num
        
        return -1
        
        