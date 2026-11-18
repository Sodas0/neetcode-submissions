class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # should prioritize based on highest frequency of tasks in list.
        # maintain a maxheap of (frequency, task) pairs.
            # at each cycle (iteration), pop the top (and store the task), and subtract freq by 1 IFF it has been more than
            # or equal to n cycles since last task equaled current task.
            # not sure how to implement this
        freqs = Counter(tasks)
        heap = [-freq for freq in freqs.values()] # negating for max-heap
        cooldown = deque()
        heapq.heapify(heap)
        time = 0

        # important to note: heap will initially only have as many items to execute as there are unique tasks. 
            # this is by design, so that only instructions ready to execute will be pushed to the heap.
        while heap or cooldown:
            time += 1

            if heap:
                remaining = heapq.heappop(heap) + 1 # + 1 because we have negated values, so adding 1 effectively subtracts 1.
                if remaining != 0:
                    cooldown.append((remaining, time+n)) # time+n is the time when this task will be executed next.
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
                
        return time