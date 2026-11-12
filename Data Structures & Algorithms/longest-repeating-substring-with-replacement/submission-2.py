class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        freq = defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            # while difference between current substring length and the most frequent element in substring exceeds # of replacements we can make
                # we want to shrink window.
            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest