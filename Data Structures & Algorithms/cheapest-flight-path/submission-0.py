class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightMap = defaultdict(list)
        for source, desti, price in flights:
            flightMap[source].append((desti, price))
        visited = {}
        heap = [(0, src, 0)]
        while heap:
            cost, city, stops = heapq.heappop(heap)
            if city == dst:
                return cost
            if (city, stops) in visited and visited[(city, stops)] <= cost:
                continue
            visited[(city, stops)] = cost
            if stops <= k:
                for next_city, next_cost in flightMap[city]:
                    heapq.heappush(heap, (cost+next_cost,next_city,stops+1))
        return -1