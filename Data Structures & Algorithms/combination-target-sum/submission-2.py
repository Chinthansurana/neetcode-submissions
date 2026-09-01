class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break
                
                path.append(nums[i])
                backtrack(i, path, remaining - nums[i])
                path.pop()
        backtrack(0, [], target)
        return res