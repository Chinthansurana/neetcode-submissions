class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxval = max(freq.values())
        bucket = [[] for _ in range(maxval+1)]
        for ele, cnt in freq.items():
            bucket[cnt].append(ele)
        res = []
        for freq in range(maxval, 0, -1):
            res.extend(bucket[freq])
            if len(res) >= k:
                break
        return res


        