class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # all possible subsets, nums has unique integers
        res = []

        # dfs function should take index of nums as param, as well as current path.
        # dfs on implicit decision tree.

        def dfs(index, path):
            # base case: we have run out of indices to make a decision at.
            if index == len(nums): #note len(nums) and not len(nums)-1
                res.append(path[:]) # a sliced copy of path.
                return # return otherwise paths will get messed up
            
            # case 1: take at current option
            path.append(nums[index])
            dfs(index+1,path)
            path.pop()

            # case 2: skip current option
            dfs(index+1,path)
        dfs(index=0, path=[])
        return res

