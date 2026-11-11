class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set for fast lookups (O(1))
        seen = set(nums)
        best = 0

        for num in seen:
            if num-1 not in seen:
                length = 1
                while num+length in seen:
                    length += 1
                best = max(best, length)
        
        return best
