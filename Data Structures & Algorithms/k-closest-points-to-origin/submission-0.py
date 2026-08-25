class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(x,y):
            return ((x*x) + (y*y)) ** (0.5)
        
        heap = []
        for point in points:
            heap.append((getDist(point[0], point[1]), point))
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res        