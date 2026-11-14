class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        freq2 = Counter()
        for r in range(len(s2)):
            freq2[s2[r]] += 1 #populate freq2
            if r>=len(s1): #if we are dealing with substring bigger than s1, we need to slide the window (remove leftmost)
                freq2[s2[r-len(s1)]] -= 1
            if freq1 == freq2:
                return True
        return False

