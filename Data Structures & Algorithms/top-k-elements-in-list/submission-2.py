class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort Approach
        numCnt = Counter(nums)
        maxVal = max(numCnt.values())
        bucket = [[] for _ in range(maxVal+1)] 
        for num, cnt in numCnt.items():
            bucket[cnt].append(num)
        res = []
        for i in range(maxVal, 0, -1):
            res.extend(bucket[i])
            if len(res) >= k:
                break
        return res
