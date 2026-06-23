class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for this problem, we can use a fixed sliding window of size len(s1).
        # initially compute frequency map of characters in s1.
        # the idea is start left pointer at 0, and start right pointer at len(s1)-1 using range fn.
        # if the freq map of characters in the window != freq_map_s1, then move window by 1 (incrememt both pointers)
        # also need to check if right pointer is at the last element of s2, if it is, we must terminate and return false.
        
        # compute s1 frequency map
        s1_freq_map = {}
        for i in range(len(s1)):
            s1_freq_map[s1[i]] = s1_freq_map.get(s1[i],0)+1
        

        left = 0
        window_freq_map = {}
        
        # window loop
        for right in range(len(s2)): 
            window_freq_map[s2[right]] = window_freq_map.get(s2[right],0)+1

            # first ensure that window size is good
            window_size = right-left+1
            if window_size < len(s1):
                # increment right pointer
                continue
        

            # here if window size is correct.
            # check if window_freq_map == s1_freq_map
            if window_freq_map == s1_freq_map:
                return True
           
            window_freq_map[s2[left]] -= 1 # decrement frequency of left pointer before moving it up.
            if window_freq_map[s2[left]] == 0:
                del window_freq_map[s2[left]]
            
            left +=1
        
        return False




            


        
 



# Input: s1 = "abcc", s2 = "leccabbee". # "ccab" is perm of "abcc".
# so if a window contains a permutation of s1, its frequency map of all characters must also match.
