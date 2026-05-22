class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)
        for num in numset:
            if num-1 not in numset:
                cur = 1
                while num + cur in numset:
                    cur+=1
                res = max(res, cur)
        return res