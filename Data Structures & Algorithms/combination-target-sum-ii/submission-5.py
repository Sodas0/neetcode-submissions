class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates_sorted = sorted(candidates)
        

        def dfs(start, path, pathsum):
            if pathsum == target:
                out.append(path.copy())
            
            elif pathsum > target:
                return
        
            else:
                for i in range(start, len(candidates_sorted)):
                    if i > start and candidates_sorted[i] == candidates_sorted[i-1]: # condition for dupe
                        continue
                    else:
                        path.append(candidates_sorted[i])
                        pathsum+=candidates_sorted[i]
                        dfs(i+1, path, pathsum)
                        path.pop()
                        pathsum-=candidates_sorted[i]

        dfs(start=0, path=[], pathsum=0)
        return out