class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        used = [False]*len(nums)
        numsSorted = sorted(nums) # design choice -- i didn't think to use numsSorted. mistake.

        def dfs(path): # i initially used start, path as params. mistake. understand why these mistakes were made.
            if len(path) == len(nums):
                out.append(path.copy())
            
            for i in range(len(nums)): 
                if i>0 and numsSorted[i] == numsSorted[i-1] and not used[i-1]: #skip cond
                    continue
                
                elif not used[i]:
                    used[i] = True
                    path.append(numsSorted[i])
                    dfs(path)
                    path.pop()
                    used[i] = False
        
        dfs(path=[])
        return out