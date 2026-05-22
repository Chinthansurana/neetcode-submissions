class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            target = -nums[i]
            while left<right:
                cur = nums[left] + nums[right]
                if cur == target:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1 
                    right -= 1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1 
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif cur > target:
                    right -= 1
                else:
                    left += 1
        return res

                    
                    

