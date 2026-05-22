class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lmax = height[l]
        rmax = height[r]
        res = 0

        while l<=r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                res += (lmax - height[l])
                l+=1
            else:
                rmax = max(rmax, height[r])
                res += (rmax-height[r])
                r-=1
        return res
