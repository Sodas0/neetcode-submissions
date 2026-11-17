class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones] # negate to make maxheap since minheap is default behavior
        heapq.heapify(heap)
        while len(heap)>1: # if 1 stone left, process is over
            first, second = -heapq.heappop(heap), -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -(first-second))
        return -heap[0] if heap else 0




