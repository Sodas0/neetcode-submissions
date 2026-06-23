class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # maximum amt a container can store-->track a variable and use max()
        # max_so_far = 0
        # # amt of water a container can store = height of smaller bar * distance between indices of bars
        
        # # can't sort the array as that would break the distance metric.


        # # brute force approach: fix a bar, and then check every other bar and compute water for each.

        # for i in range(len(heights)):
        #     for j in range(1,len(heights)):
        #         # dont compute water for same index
        #         if i==j:
        #             continue
                
        #         water = min(heights[i],heights[j])*(j-i)
        #         max_so_far = max(max_so_far,water)

        # return max_so_far
            
        # optimal approach:
            # realize that amt of water is determined by distance between bars and the shorter of the two bars.
            # moving pointers inwards means we lose width that we can't get back. Losing width means losing area.
            # the solution to this is always move the shorter bar and track the max. I believe this will give us the optimal solution.
        max_so_far = 0
        left, right = 0, len(heights)-1

        while left < right:
            # first compute area.
            area = min(heights[left], heights[right])*(right-left)
            max_so_far = max(area,max_so_far) # track the max area seen globally
            if heights[left] < heights[right]: # left is shorter
                left +=1
            else: #right is shorter
                right -=1
        
        return max_so_far
