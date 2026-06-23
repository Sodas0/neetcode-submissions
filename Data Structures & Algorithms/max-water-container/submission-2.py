class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # trick here is that we recognize to calculate the area, we need:
        #  min(heights[right] , heights[left]) * (right - left)
        # maintain a running max_area.
        # start pointers left at 0, and pointer right at len(heights)-1
        # compute area intermediately, update max_area if it is new max.
        # the check is to see which height is smaller. If left is smaller, increment left, otherwise, decrement right.

        left,right,max_area = 0,len(heights)-1,0

        while left<right: # pointers meet at middle
            # first compute area and store new max
            area = min(heights[left], heights[right])*(right-left)
            max_area=max(max_area,area)
            if heights[left]<heights[right]:
                left+=1
            else:right-=1

        
        return max_area