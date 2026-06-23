class Solution:
    def isPalindrome(self, s,i,j):
        while i<j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True 

    
    def partition(self, s: str) -> List[List[str]]:
        output = []
        partitions = []

        def dfs(i):
            # base case
            if i >= len(s):
                output.append(partitions[:]) # or .copy()
                return
            
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    partitions.append(s[i:j+1])
                    dfs(j+1)
                    partitions.pop()

        dfs(0)
        return output

