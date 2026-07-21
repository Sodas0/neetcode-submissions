class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n    = len(nums)
        out  = []
        used = [False]*n

        def dfs(path):
            if len(path) == n:
                out.append(path.copy())
            else:
                for i in range(n):
                    if not used[i]: # used[i] is False 
                        path.append(nums[i])
                        used[i] = True
                        dfs(path)
                        path.pop()
                        used[i] = False
        
        dfs(path=[])
        return out