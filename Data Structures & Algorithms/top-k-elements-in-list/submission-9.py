class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = defaultdict(list)

        for ele, cnt in freq.items():
            bucket[cnt].append(ele)
        
        res = []
        for i in range(len(nums), 0, -1):
            res.extend(bucket[i])
            if len(res) >= k:
                return res[:k]