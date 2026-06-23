class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea is to use a dynamic sliding window to keep track of max_profit_so_far, where the size of the window is determined by if price goes down or up on the i+1th day.
        left = 0
        max_profit = 0

        for right in range(1,len(prices)):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right]-prices[left])
            else: # right is less than left -- no profit to be had, so set left to right.
                left = right
            
        return max_profit