class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(start, path):
            # collect results intermediately
            output.append(path[:])

            #iterate over levels
            for i in range(start, len(nums)):
                path.append(nums[i]) # take
                dfs(i+1,path) # recurse
                path.pop() # undo during unwind
            
        dfs(start=0,path=[])
        return output
