class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i remember this one -- two pointers at either end. use property that it is non-decreasing to either decrement j if sum is too high, or increment i if sum is too low.
        i,j = 0, len(numbers)-1
        while i<j:
            if numbers[i] + numbers[j] < target: # if less than target, increment i
                i+=1
            elif numbers[i] + numbers[j] > target: # if greater than target, decrement j
                j-=1
            else: #match
                return [i+1,j+1]


        # return 1 indexed -- just add 1 to found indices at the end