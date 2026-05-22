class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_arr = [1] * n
        prefix = 1
        for i in range(n):
            pref_arr[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in reversed(range(n)):
            pref_arr[i] *= postfix
            postfix *= nums[i]
        return pref_arr