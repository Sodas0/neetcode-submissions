class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0] # initially the first word
        
        for string in strs:
            if not string:
                return ""
            for i in range(min(len(prefix),len(string))):
                print(i, prefix[i], string[i])
                if prefix[i] != string[i]:
                    prefix = string[0:i]
                    break
                else:
                    prefix=prefix[:len(string)]
        
        return prefix