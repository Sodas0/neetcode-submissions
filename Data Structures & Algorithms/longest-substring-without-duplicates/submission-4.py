class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen: # if right ptr value is in seen, it's a duplicate - fix window immediately by shrinking from left and removing l ptr vals from set
                seen.remove(s[l])
                l+=1
            seen.add(s[r]) # still need to add s[r] 
            max_len=max(max_len,r-l+1) # +1 because len is 1-indexed
        return max_len
            