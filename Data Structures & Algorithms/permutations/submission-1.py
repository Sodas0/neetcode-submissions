class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        used = [False]*len(nums)
        
        def dfs(path):
            if len(path) == len(nums):
                out.append(path.copy())
            else:
                for i in range(len(nums)):
                    if not used[i]: # if used[i] is false:
                        path.append(nums[i])
                        used[i] = True
                        dfs(path)
                        path.pop()
                        used[i] = False
        
        dfs(path=[])
        return out
