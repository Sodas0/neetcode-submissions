class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []

        sortedCands = sorted(candidates)

        def dfs(start, path, pathsum):
            if pathsum == target:
                out.append(path.copy())
            elif pathsum > target:
                return
            else:
                for i in range(start, len(sortedCands)):
                    if i > start and sortedCands[i] == sortedCands[i-1]: # adjacent sortedCands are duplicates. we can skip.
                        continue
                    else:
                        path.append(sortedCands[i])
                        pathsum+=sortedCands[i]
                        dfs(i+1,path,pathsum) # start=i+1 because we can take at most one candidate in a combination.
                        path.pop()
                        pathsum-=sortedCands[i]
                
        dfs(start=0,path=[],pathsum=0)
        return out