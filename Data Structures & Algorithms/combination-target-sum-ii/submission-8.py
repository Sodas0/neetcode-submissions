class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # subsets/combinations = start, no used.
        out = []
        # dupes possible in construction of results, so need to sort to prevent.
        sortCands = sorted(candidates)
        
        def dfs(start, path, pathsum):
            # collection mechanism
            if pathsum == target:
                out.append(path.copy())
            if pathsum > target:
                return
            
            for i in range(start, len(sortCands)):
                # guard duplicate combinations
                if i > start and sortCands[i] == sortCands[i-1]:
                    continue
                path.append(sortCands[i])
                pathsum+=sortCands[i]
                dfs(i+1, path, pathsum)
                path.pop()
                pathsum-=sortCands[i]
        
        dfs(start = 0, path = [], pathsum = 0)
        return out

# [9,2,2,4,6,1,5]
# [1,2,2,4,5,6,9]
        
# [2,2,4] == 8
