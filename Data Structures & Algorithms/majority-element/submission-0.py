class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        
        # find highest by sorting.
        # print(sorted(freq_map.items()))
        sorted_freq = (sorted(freq_map.items(),key=lambda x: x[1],reverse=True))
        print(sorted_freq)
        return sorted_freq[0][0]