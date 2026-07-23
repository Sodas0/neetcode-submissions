class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def isPalindrome(string):
            left, right = 0, len(string)-1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def dfs(start, path):
            if start == len(s):
                out.append(path.copy())
            
            for i in range(start, len(s)):
                substring = s[start:i+1]
                if isPalindrome(substring):
                    path.append(substring)
                    dfs(i+1,path)
                    path.pop() 
        
        dfs(start=0, path=[])
        return out
