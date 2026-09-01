class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, path):
            if len(path) <= len(nums):
                res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res