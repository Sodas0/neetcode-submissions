class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  keep track of frequency of letters -- need to construct freq map for both strings.
        s_map, t_map = {}, {}
        for character in s: # iterate through each character in string s
            if character not in s_map: # check if first time seeing character
                s_map[character] = 1 # set freq to 1 
            else: # if not first time seeing character -- it must already be in map
                s_map[character] += 1 #increment freq by 1
        
        # same thing for t
        for character in t: # iterate through each character in string s
            if character not in t_map: # check if first time seeing character
                t_map[character] = 1 # set freq to 1 
            else: # if not first time seeing character -- it must already be in map
                t_map[character] += 1 #increment freq by 1

        
        # now need to check if s_map and t_map are same.
        return s_map == t_map