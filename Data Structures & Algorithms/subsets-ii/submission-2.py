class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        numsSorted = sorted(nums) # implicitly handles used..?

        def dfs(start, path):
            # collection at every unique path
            out.append(path.copy())

            for i in range(start, len(numsSorted)):
                if i > start and numsSorted[i] == numsSorted[i-1]:
                    continue
                #otherwise, we can apply the backtracking:
                path.append(numsSorted[i])
                dfs(i+1, path)
                path.pop()
        dfs(start=0, path=[])
        return out
                