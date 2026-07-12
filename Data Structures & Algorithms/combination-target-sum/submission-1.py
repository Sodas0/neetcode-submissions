class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        def dfs(index, path, pathsum):
            # base case should be if pathsum  == target
            if pathsum == target:
                out.append(path.copy())
            
            elif pathsum > target: # can just prune the rest since it's no longer useful to consider
                return
            
            else: # now we consider taking other options.
                for i in range(index, len(nums)):
                    pathsum+=nums[i]
                    path.append(nums[i])
                    dfs(i,path,pathsum) # not i+1 because "unlimited times"
                    pathsum-=nums[i]
                    path.pop()
        
        dfs(index=0,path=[],pathsum=0)
        return out
