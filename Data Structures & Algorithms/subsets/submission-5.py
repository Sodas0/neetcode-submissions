class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(start, path):
            out.append(path.copy()) # don't mutate path directly in recursion

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i+1,path) 
                path.pop() # undo the backtracking
        
        dfs(start=0, path=[])
        return out