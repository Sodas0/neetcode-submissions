class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, longest = 0,0
        for r in range(len(s)):
            while s[r] in seen: # duplicate detected, shrink window from left until no longer the case.
                seen.remove(s[l])
                l+=1
            # now add s[r] to seen
            seen.add(s[r])
            longest = max(longest, r-l+1) #+1 because r-l is just the gap, we need to account for the current addition
        return longest