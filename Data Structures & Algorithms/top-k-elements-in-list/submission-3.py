class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        heap = [[-cnt, ele] for ele, cnt in freq.items()]
        heapq.heapify(heap)
        for _ in range(k):
            _, ele = heapq.heappop(heap)
            res.append(ele)
        return res