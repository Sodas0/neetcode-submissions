class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # all possible subsets, nums has unique integers
        res = []

        # dfs function should take index of nums as param, as well as current path.
        # dfs on implicit decision tree.

        def dfs(index, path):
            # collect to res at every valid node:
            res.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                print(f"path: {path}")
                dfs(i+1,path)
                path.pop()
                print(f"path after pop(): {path}")
                
        dfs(index=0,path=[])
        return res

