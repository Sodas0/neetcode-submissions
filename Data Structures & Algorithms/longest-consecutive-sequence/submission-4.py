class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # insight: set for fast lookups. for each number in the sequence, if that number-1 is not in the set, it's not a valid start for the sequence
        seen = set(nums)
        longest = 0

        for num in seen:
            if num-1 not in seen:
                length = 1

                while num+length in seen:
                    length += 1
                
                longest = max(longest, length)
        return longest