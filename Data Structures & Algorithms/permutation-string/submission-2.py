class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # need a helper to check permutation (aka anagram)
        def isAnagram(sub1, sub2):
            if len(sub1) != len(sub2):
                return False
            freq1 = Counter(sub1)
            freq2 = Counter(sub2)
            return freq1 == freq2
        
        # my idea is that we can use a freq map of s1 as a 'key' and then a fixed size sliding window
        # across s2. if theres a match, good, if not, return False
        l,r = 0,len(s1)-1
        while r<len(s2):
            if isAnagram(s1, s2[l:r+1]):
                return True
            else:
                l+=1
                r+=1
        return False
