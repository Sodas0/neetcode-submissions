class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # important thing is to sort it so iteration behavior becomes predictable.
        nums = sorted(nums)
        out = []

        # notion here is to fix outer loop.
        for i in range(len(nums)):
            # check for duplicate pointer values
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1

            while left < right:
                # check for sum.
                temp = nums[i] + nums[left] + nums[right]

                if temp < 0: # need to increment left.
                    left+=1
                elif temp >0:
                    right-=1
                else:
                    out.append([nums[i] , nums[left] , nums[right]])
                    left+=1
                    right-=1
                
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        return out