class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * (n)

        pref = 1
        for i in range(n):
            res[i] = pref
            pref *= nums[i]
        
        postf = 1
        for i in range(n-1, -1, -1):
            res[i] *= postf
            postf *= nums[i]
        
        return res