class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build freq of nums
        freq = Counter(nums)
        heap = []
        for num, count in freq.items(): 
            heapq.heappush(heap, (count, num)) #### important: we want heap to compare by freq first, not the number itself.
            if len(heap)>k: # pop min (root), since the heap would then only contain top k frequent elemenets once freq is exhausted.
                heapq.heappop(heap)
        return [num for count, num in heap]


