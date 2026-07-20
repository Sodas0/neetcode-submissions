class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums_sorted = sorted(nums)

        def dfs(start, path):
            out.append(path.copy())
            # print(f"out: {out}")
            for i in range(start, len(nums_sorted)):
                if i>start and nums_sorted[i] == nums_sorted[i-1]:
                    continue # i think continue instead of return.
                else:
                    path.append(nums_sorted[i])
                    dfs(i+1, path)
                    path.pop()

                
        
        dfs(start=0, path=[])
        return out