class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(start, path):
            out.append(path.copy())

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        
        dfs(start=0, path=[])
        return out