class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maximum amt a container can store-->track a variable and use max()
        max_so_far = 0
        # amt of water a container can store = height of smaller bar * distance between indices of bars
        
        # can't sort the array as that would break the distance metric.


        # brute force approach: fix a bar, and then check every other bar and compute water for each.

        for i in range(len(heights)):
            for j in range(1,len(heights)):
                # dont compute water for same index
                if i==j:
                    continue
                
                water = min(heights[i],heights[j])*(j-i)
                max_so_far = max(max_so_far,water)

        return max_so_far
            

# initially i = 0