class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, tar, path):
            if tar == 0:
                result.append(path)
                return

            for i in range(start, len(nums)):
                if nums[i] > tar:
                    break
                backtrack(i ,tar-nums[i], path+[nums[i]])
        nums.sort()
        result = []
        backtrack(0, target, [])
        return result