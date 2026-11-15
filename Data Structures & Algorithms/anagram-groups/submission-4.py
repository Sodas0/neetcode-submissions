class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ###O(n*klogk) approach
        freqs = defaultdict(list)
        res = []
        # build a frequency map that stores data as freqs['sort'] = ['original1', 'original2'] 
            # where the key corresponds to the sorted version of each string
        for string in strs:
            sort = ''.join(sorted(string))
            freqs[sort].append(string)
    
        return list(freqs.values())
