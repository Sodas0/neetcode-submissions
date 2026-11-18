class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap. pop from the heap until the length of it is < k. resulting root will be kth largest.
        heap = nums[:] # shallow copy 
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        return heap[0]
