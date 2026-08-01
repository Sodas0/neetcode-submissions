class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        used = [False]*len(nums)

        def dfs(path):
            if len(path) == len(nums):
                out.append(path.copy())

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
                    used[i] = False
            
        dfs(path=[])
        return out