class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v, w))
        
        stops = [float('inf')] * n
        heap = [(0, src, 0)]

        while heap:
            cost, city, edges = heapq.heappop(heap)
            print(cost, city, edges)
            if city == dst:
                return cost
            
            if edges == k+1:
                continue
            
            if stops[city] <= edges:
                continue
            stops[city] = edges
            for nei, newcost in graph[city]:
                heapq.heappush(heap, (cost+newcost, nei, edges+1))
        return -1