class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        # since this is subsets problem, we should use sorted nums to force increasing order
        numsSorted = sorted(nums)

        def dfs(start, path):
            # collection pattern: collect at every unique subset
            out.append(path.copy())

            for i in range(start, len(numsSorted)):
                # at this level of recursion, have we already explored and created trees for numsSorted, so we can safely skip
                # dupes.
                if i > start and numsSorted[i] == numsSorted[i-1]: 
                    continue
                
                path.append(numsSorted[i])
                dfs(i+1, path)
                path.pop()
            
        dfs(start=0, path=[])
        return out