class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def isPalindrome(string) -> bool:
            i,j = 0, len(string)-1
            while i < j:
                if string[i] != string[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def dfs(start, path):
            if start == len(s):
                out.append(path.copy())
            
            for i in range(start, len(s)):
                substr = s[start:i+1]
                if isPalindrome(substr):
                    path.append(substr)
                    dfs(i+1,path)
                    path.pop()

        dfs(start=0, path=[])
        return out