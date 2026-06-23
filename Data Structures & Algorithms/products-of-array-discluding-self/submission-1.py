class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create output, size = len(nums)
        output = [0] * len(nums)

        # iterate through output array to begin setting values
       
        for i in range(len(output)):
            product = 1
            # need to iterate through nums for every pass through output.
            for j in range(len(nums)):
                if j!=i:
                    product *= nums[j]
            
            output[i] = product

        return output

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = [0] * len(nums)

#         for i in range(len(nums)):
#             product = 1
#             for j in range(len(nums)):
#                 if j != i:
#                     product *= nums[j]
#             output[i] = product

#         return output
