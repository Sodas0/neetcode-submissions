class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 2 anagrams, when sorted, should be equal to each other when comparing strings.
        # add them to a freq and return the original strings of each sorted one
        res = []
        freq = defaultdict(list)
        for string in strs:
            sortedstring = ''.join(sorted(string))
            freq[sortedstring].append(string)

        for item in freq.items():
            res.append(item[1])
        return res


