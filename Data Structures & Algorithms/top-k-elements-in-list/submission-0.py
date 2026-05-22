class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-cnt, ele) for ele, cnt in freq.items()]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            _, cur = heapq.heappop(heap)
            res.append(cur)
        return res