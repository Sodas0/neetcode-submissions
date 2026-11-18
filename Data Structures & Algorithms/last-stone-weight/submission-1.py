class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # negate each one for max-heap setup
        heapq.heapify(stones) # min heap by default; so we use negated values.
        while len(stones)>1:
            first, second = -heapq.heappop(stones), -heapq.heappop(stones) # revert to original val for calcs
            if first != second:
                heapq.heappush(stones, -(first - second))
        return -stones[0] if stones else 0        