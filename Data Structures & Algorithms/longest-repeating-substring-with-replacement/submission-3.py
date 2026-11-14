class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        best_so_far = 0
        l = 0
        for r in range(len(s)):
            freq_map[s[r]] += 1
            while (r-l+1)-max(freq_map.values())>k: # while there are letters that cannot be replaced by k operations
                freq_map[s[l]] -= 1
                l += 1
            #bookkeep 
            best_so_far = max(best_so_far, r-l+1)
        return best_so_far