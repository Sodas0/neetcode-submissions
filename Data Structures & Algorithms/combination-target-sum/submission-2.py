class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        def dfs(start, path, pathsum):
            if pathsum == target:
                out.append(path.copy())
            elif pathsum>target:
                return
            else:
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    pathsum+=nums[i]
                    dfs(i,path,pathsum) # i because we can take same # more than once
                    path.pop()
                    pathsum-=nums[i]
        
        dfs(start=0,path=[],pathsum=0)
        return out