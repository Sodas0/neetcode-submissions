class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # basically maintain a min heap where the min heap is based on distance to origin based on the formula.
        origin_dists = []
        for pair in points:
            p1,p2 = pair[0],pair[1]
            dist = math.sqrt((p1-0)**2 + (p2-0)**2)
            origin_dists.append((dist, pair))

        heapq.heapify(origin_dists)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(origin_dists)[1])
        
        return res
