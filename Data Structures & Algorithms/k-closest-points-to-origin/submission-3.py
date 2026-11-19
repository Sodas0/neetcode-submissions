class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            dist = math.sqrt((x-0)**2 + (y-0)**2)
            dists.append((dist, [x,y]))
        heapq.heapify(dists)
        out = []
        for _ in range(k):
            out.append(heapq.heappop(dists)[1])
        return out
        
