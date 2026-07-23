class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        used = [False]*len(nums)
        
        numsSorted = sorted(nums)

        def dfs(path):
            if len(path) == len(numsSorted):
                out.append(path.copy())
            
            for i in range(len(nums)):
                if i>0 and numsSorted[i] == numsSorted[i-1] and not used[i-1]:
                    continue

                if not used[i]:
                    used[i] = True
                    path.append(numsSorted[i])
                    dfs(path)
                    used[i] = False
                    path.pop()
        
        dfs(path=[])
        return out
                
