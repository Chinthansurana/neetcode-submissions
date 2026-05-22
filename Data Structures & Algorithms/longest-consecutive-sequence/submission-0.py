class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            if num-1 not in numset:
                cur = 1
                while num + cur in numset:
                    cur += 1
                longest = max(longest, cur)
        return longest