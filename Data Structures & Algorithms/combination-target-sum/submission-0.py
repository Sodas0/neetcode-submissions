class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(start,path,pathsum):
            if pathsum == target:
                output.append(path[:])
            
            if pathsum > target:
                return

            # can take multiple copies of same #
            for i in range(start, len(nums)):
                path.append(nums[i])
                pathsum+=nums[i]
                dfs(i,path,pathsum)
                path.pop()
                pathsum-=nums[i] #?

        dfs(start=0,path=[],pathsum=0)
        return output

