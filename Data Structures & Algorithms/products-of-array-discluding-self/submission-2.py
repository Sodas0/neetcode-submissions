class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        # # create output, size = len(nums)
        # output = [0] * len(nums)

        # # iterate through output array to begin setting values
       
        # for i in range(len(output)):
        #     product = 1
        #     # need to iterate through nums for every pass through output.
        #     for j in range(len(nums)):
        #         if j!=i:
        #             product *= nums[j]
            
        #     output[i] = product

        # return output

        # optimal: prefix * suffix.
        # allocate
        res = [1] * len(nums)

        # prefix pass
        prefix = 1
        for i in range(len(nums)): # go from 0 to i-1
            res[i] = prefix # 
            prefix *= nums[i]
        
        # suffix pass
        suffix = 1
        for i in range(len(nums)-1, -1,-1): # go from last index to 0, stepping backwards by -1.
            res[i] *= suffix
            suffix *= nums[i]
        return res

# eg
#.     [-1,0,1,2,3]
#res = [0,6,6,3,1]
# prefix pass:
# i in range(len(nums)): 0,1,2,3,4
# when i = 0: res[0] = 1 ; prefix *= -1 = -1 -> next iteration
# when i = 1: res[1] = -1 ; prefix *= 0 = 0 -> next iteration
# when i = 2: res[2] = 0 ; preix *= 1 = 0 -> next iteration
# when i = 3: res[3] = 0 ; prefix *= 2 = 0 -> next iteration
# when i = 4: res[4] = 0 ; prefix *= 3 = 0 -> end iter

# suffix pass:
# i in range(len(nums)-1, -1,-1): 4,3,2,1,0
# when i = 4: res[4] = 1 ; suffix *= 3 = 3 -> next iteration
# when i = 3: res[3] = 3 ; suffix *= 2 = 6 -> next iteration
# when i = 2: res[2] = 6 ; suffix *= 1 = 6 -> next iteration
# when i = 1: res[1] = 6 ; suuffx *= 0 = 0 -> next iteration
# when i = 0: res[0] = 0 ; suffix *= 0 = 0 -> end iter

