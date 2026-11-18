class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for pair in points:
            p1,p2 = pair[0],pair[1]
            dist = math.sqrt((p1-0)**2 + (p2-0)**2)
            dists.append((dist, pair))
        heapq.heapify(dists)
        out = []
        for _ in range(k):
            out.append(heapq.heappop(dists)[1])
        return out