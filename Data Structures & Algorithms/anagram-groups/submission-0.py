class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # helper to compute frequency maps for each string and store in a list. 
        def compute_freq_maps(string) -> Dict:
            freq_map = {}
            for char in string:
                if char not in freq_map:
                    freq_map[char] = 1
                else: freq_map[char] +=1
            return freq_map
        
        groups = {} # dictionary of anagrams that are identical. key = sorted anagram; value = str
        
        for string in strs: # for each string -- compute freq maps, sort the keys
            freq_map =  compute_freq_maps(string)

            key = tuple(sorted(freq_map.items())) # tuple because dicts are not hashable. ensures that duplicate anagrams compute the same keys.

            if key not in groups: #if first time seeing the anagram, make an empty list to store the groups
                groups[key] = []
            groups[key].append(string)
            
        
        return list(groups.values())
        
       

        

