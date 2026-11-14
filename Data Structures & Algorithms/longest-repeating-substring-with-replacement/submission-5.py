class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left, best = 0, 0
        for right in range(len(s)):
            freq[s[right]] += 1
            # invariant: while length of current substring cannot have same letters with more than k replacements
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
            


