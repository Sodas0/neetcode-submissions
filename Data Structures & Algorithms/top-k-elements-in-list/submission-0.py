class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make frequency map -- key = value ; value = freq
        freq_map = {}
        for i in range(len(nums)):
            if nums[i] not in freq_map: # if first time seeing a value, add it to freq map with freq = 1
                freq_map[nums[i]] = 1
            else: # otherwise, it must already have been seen, so increment it
                freq_map[nums[i]] += 1
        
        # ok now that freq map is generated, tricky part is to return the keys from the sorted values.
        # insight: use lambda function as key param in sorted() function.
        sorted_nums = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True) #lambda function here is basically saying sort the keys based on the value of frequencies.

        return sorted_nums[:k]

                