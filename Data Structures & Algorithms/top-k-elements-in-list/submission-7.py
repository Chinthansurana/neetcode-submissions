class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        heap = [(-freq, ele) for ele, freq in freqMap.items()]
        heapq.heapify(heap)
        res = []

        while k:
            _, ele = heapq.heappop(heap)
            res.append(ele)
            k -= 1
        return res
        