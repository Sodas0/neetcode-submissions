class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        used = [False]*len(nums)

        def dfs(path):
            if len(path) == len(nums):
                out.append(path.copy())
            else:
                for i in range(len(nums)):
                    if not used[i]:
                        used[i] = True
                        path.append(nums[i])
                        dfs(path)
                        used[i] = False
                        path.pop()
        
        dfs(path=[])
        return out