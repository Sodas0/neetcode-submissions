class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # variable size sliding window
        seen = set()
        l = 0
        longest = 0 
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l]) # idea is that if we are breaking the condition for substring, we remove from left until we're valid
                l+=1
            seen.add(s[r])
            longest = max(longest, r-l+1)
        return longest


                
