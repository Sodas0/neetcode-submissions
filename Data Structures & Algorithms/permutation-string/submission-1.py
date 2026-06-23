class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use a fixed size sliding window of size len(s1)
        # use the freq map of s1 and compare that to freq map of window.
        # if the window does not contain freq map, repeat until either it does or we have iterated through s2.
        s1_map = Counter(s1)
        s2_map = Counter()
        
        if len(s1) > len(s2): 
            return False # s2 cant contain substrings if it is itself smaller than s1.
        
        for i in range(len(s2)):
            s2_map[s2[i]] += 1
            if i >= len(s1):
                if s2_map[s2[i - len(s1)]] > 1:
                    s2_map[s2[i - len(s1)]] -= 1                    
                else:
                    del s2_map[s2[i - len(s1)]]
            if s1_map == s2_map:
                return True 

        return False