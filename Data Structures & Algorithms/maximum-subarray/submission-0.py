class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = currsum = nums[0]
        for num in nums[1:]:
            currsum = max(num + currsum, num)
            maxsum = max(currsum, maxsum)
        return maxsum