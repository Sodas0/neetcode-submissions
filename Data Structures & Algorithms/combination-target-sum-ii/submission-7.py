class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        # for combinations, use sorted array & used list. 
        sortCands = sorted(candidates)
        
        def dfs(start, path, pathsum):
            # collection when pathsum = target
            if pathsum == target:
                out.append(path.copy())
            if pathsum > target:
                return
                
            for i in range(start, len(sortCands)):
                # duplicate combination guard
                if i > start and sortCands[i] == sortCands[i-1]:
                    continue
                
                path.append(sortCands[i])
                pathsum+=sortCands[i]
                dfs(i+1, path, pathsum)
                path.pop()
                pathsum-=sortCands[i]
        
        dfs(0, [], 0)
        return out