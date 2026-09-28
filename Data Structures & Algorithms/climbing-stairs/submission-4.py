class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, prev1 = 2, 1 
        for i in range(3, n+1):
            prev1, prev = prev, prev1+prev

        return prev