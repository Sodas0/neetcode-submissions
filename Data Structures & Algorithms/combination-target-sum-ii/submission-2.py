class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        
        # sort the candidates to force ascending order in recursion
        sort = sorted(candidates)

        def dfs(start, path, pathsum):
            if pathsum == target:
                out.append(path.copy())
            elif pathsum > target:
                return
            else:
                for i in range(start, len(sort)):
                    if i > start and sort[i] == sort[i-1]:
                        continue
                    else:
                        path.append(sort[i])
                        pathsum+=sort[i]
                        dfs(i+1, path, pathsum)
                        path.pop()
                        pathsum-=sort[i]
                    
        
        dfs(start=0, path=[], pathsum=0)
        return out