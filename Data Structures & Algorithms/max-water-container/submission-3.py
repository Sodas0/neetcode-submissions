class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = base*height
        # container is determined by height of smaller one always.
        best_so_far = 0
        l,r = 0, len(heights)-1
        while l<r:
            area = min(heights[l], heights[r])*abs(l-r)
            best_so_far = max(best_so_far, area)
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                r-=1 # arbitrary tie breaker
        return best_so_far