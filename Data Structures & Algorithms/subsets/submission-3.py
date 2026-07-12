class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(index, path): # keep track of the path at each level
            # collect each new path to out.
            out.append(path.copy()) # copy because we don't want to mutate path itself

            for i in range(index, len(nums)):
                path.append(nums[i]) # take
                dfs(i+1,path) # recurse
                path.pop() # pop (backtrack)
                
        
        dfs(index = 0, path=[])
        return out