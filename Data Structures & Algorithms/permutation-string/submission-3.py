class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # my idea is that we can use a freq map of s1 as a 'key' and then a fixed size sliding window
        # across s2. if theres a match, good, if not, return False
        freq1 = Counter(s1)        
        l,r = 0,len(s1)-1
        while r<len(s2):
            freq2 = Counter(s2[l:r+1])
            if freq1 == freq2:
                return True
            else:
                l+=1
                r+=1
        return False
