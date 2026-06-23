class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_so_far = 0
        for num in nums_set:
            if num-1 not in nums_set: # we have a candidate
                checker = num # keep track of the sequence using a new variable starting at the value of num
                # continuously check if sequence persists
                while checker in nums_set:
                    checker+=1 #increment if it is, and check again
                # if here, then sequence broke, so set longest_so_far
                longest_so_far = max(longest_so_far, checker-num) #can use checker-num for length of sequence since we are incrementing by 1 each time. Also because this implicitly handles 1-index.
        return longest_so_far


### PATTERN FOR longest consecutive sequence:
    # use set, and track longest length so far.
    # The trick is to realize that if a number in the set - 1 is not in the set -- then we have a candidate to start checking.
    # intuition: if a number-1 IS in the set -- it is no longer the start of a sequence, so we ignore it.
    # then it comes down to tracking the difference and setting answer based on the max between previous iterations and the current candidate length.
