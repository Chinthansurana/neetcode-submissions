class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-ele for ele in freq.values()]
        heapq.heapify(heap)

        res = 0
        q = deque()

        while heap or q:
            res += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, res+n])
            if q and q[0][1] == res:
                heapq.heappush(heap, q.popleft()[0])
        return res