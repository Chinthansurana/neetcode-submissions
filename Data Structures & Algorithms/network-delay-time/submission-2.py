class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0

        heap = [(0, k)]
        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue
            # dist[node] = d

            for v, weight in graph[node]:
                nw = weight+d
                if nw < dist[v]:
                    dist[v] = nw
                    heapq.heappush(heap, (nw, v))

        res = max(dist[1:])
        return res if res != float('inf') else -1