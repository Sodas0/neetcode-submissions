class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth larget = min heap
        heap = nums[:] #shallow copy
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        return heap[0] # root after pruning heap to size k will be kth largest 