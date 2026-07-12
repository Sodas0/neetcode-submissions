class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(floor, path):
            out.append(path.copy())

            for i in range(floor, len(nums)):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()

        dfs(floor=0, path=[])
        return out
