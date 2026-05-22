class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        mheap = [(-occ, ele) for ele, occ in freq.items()]
        heapq.heapify(mheap)
        while k:
            _, ele = heapq.heappop(mheap)
            res.append(ele)
            k-=1
        return res