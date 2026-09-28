class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dfs(num):
            prev = prev1 = 0
            for i in range(len(num)):
                prev1, prev = prev, max(prev, num[i]+prev1)
            return prev
        return max(dfs(nums[1:]), dfs(nums[:-1]))