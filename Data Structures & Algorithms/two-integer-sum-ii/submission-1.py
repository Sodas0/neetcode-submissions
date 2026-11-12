class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non decreasing order.
        # this means that if ind1+ind2 > target, ind2 must be too high and therefore we decrement it, and vice versa.
        l, r = 0, len(numbers)-1
        while l<r:
            s = numbers[l]+numbers[r]
            if s == target:
                return [l+1,r+1]
            elif s<target:
                l+=1
            else:
                r-=1
          