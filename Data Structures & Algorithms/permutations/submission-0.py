class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        used = [False]*len(nums)

        def dfs(path):
            # a permutation is only complete if the path is len of nums.
            if len(path) == len(nums):
                out.append(path.copy())
            
            for i in range(len(nums)):
                if not used[i]: # if used[i] is False, we add to path
                    path.append(nums[i])
                    used[i] = True
                    dfs(path)
                    path.pop()
                    used[i] = False
                

        dfs(path=[])
        return out