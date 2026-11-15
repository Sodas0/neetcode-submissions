class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ###O(n*klogk) approach (sort)
        # freqs = defaultdict(list)
        # res = []
        # # build a frequency map that stores data as freqs['sort'] = ['original1', 'original2'] 
        #     # where the key corresponds to the sorted version of each string
        # for string in strs:
        #     sort = ''.join(sorted(string))
        #     freqs[sort].append(string)
        # return list(freqs.values())

        ### O(n*k) approach
        groups = defaultdict(list)
        for s in strs:
            counts = [0]*26 # for each string use a 26-element list for per-letter counts
            for c in s:
                counts[ord(c) - ord('a')] += 1
            groups[tuple(counts)].append(s) ### dict keys can't be lists
        return list(groups.values())


