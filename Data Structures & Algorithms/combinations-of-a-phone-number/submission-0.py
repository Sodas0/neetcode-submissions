class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        out = []

        lettermap = {
            '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'],
            '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']
        } 

        def dfs(start, path):
            if len(path) == len(digits):
                out.append(path)
            
            if start>=len(digits):
                return
            else:
                for letter in lettermap[digits[start]]:
                    dfs(start+1, path+letter)

        dfs(start=0, path="")
        return out   