class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numInd = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numInd:
                return [numInd[diff], i]
            numInd[num] = i