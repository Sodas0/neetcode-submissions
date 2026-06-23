class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start,path,pathsum):
            if pathsum == target:
                res.append(path[:])
            
            for i in range(start,len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                if pathsum > target:
                    break # nothing left in this branch
            
                path.append(candidates[i])
                pathsum+=candidates[i]
                dfs(i+1,path,pathsum)
                path.pop()
                # undo pathsum on the way up
                pathsum-=candidates[i]
        dfs(start=0,path=[],pathsum=0)
        return res
