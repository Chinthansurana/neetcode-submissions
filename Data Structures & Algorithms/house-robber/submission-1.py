class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            skip = dfs(i+1)
            rob = nums[i] + dfs(i+2)
            memo[i] = max(skip, rob)
            return memo[i]
        return dfs(0)
