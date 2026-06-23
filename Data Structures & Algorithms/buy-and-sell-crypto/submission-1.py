class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea is to track max profit so far, and use a dynamic size sliding window where size is determined by whether price goes up or down.
        # if price goes up, compute profit, set max profit to max of itself and computed profit.
        # then, we can set left pointer to right pointer.
        left = 0 # left ptr
        max_profit_so_far = 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
                # if there is profit to be had, compute the profit and set new max if it is a new max.
                max_profit_so_far = max(max_profit_so_far, prices[right]-prices[left])
            else:
                # otherwise, no profit to be had, reset window
                left = right
        return max_profit_so_far