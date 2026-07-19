class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        def dfs(start, pathsum, path):
            if pathsum == target:
                out.append(path.copy())
            elif pathsum > target:
                return
            else:
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    pathsum+=nums[i]
                    dfs(i, pathsum, path)
                    path.pop()
                    pathsum-=nums[i]
        
        dfs(start=0 ,pathsum=0 ,path=[]) # smallest case
        return out