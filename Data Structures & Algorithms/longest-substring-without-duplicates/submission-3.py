class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # idea is to use a sliding window with two pointers left and right both starting at 0.
        # keep a set that keeps track of seen characters in the current window s[l:r+1]
        # move r forward 1 step at a time and check if s[r] is in the set (duplicate)
        # combat this by moving l forward and removing s[l] from the set until s[r] is not in the set
        # once valid -- update max so far with current window length (r-l+1)
        # keep doing this until r reaches end of stirng

        l = 0
        seen = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len
        
# "zxyzxyz"
# 0 1 2 3 4 5 6  | seen = {}
# r = 0 , s[r] = z , z not in seen -> seen = {z}, max_len is 1 (0-0+1) +1 is there because length is 1-indexed.
# r = 1 , s[r] = x , x not in seen -> seen = {z,x}, max_len is 2 (1-0+1)
# r = 2 , s[r] = y , y not in seen -> seen = {z,x,y}, max len is 3 (2-0+1)
# r = 3 , s[r] = z , z IS in seen -> move to inner loop
    # s[r] = z, z is in seen, move l up until z no longer in seen
    # i get the idea/