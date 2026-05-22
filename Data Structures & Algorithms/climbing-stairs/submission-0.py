class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1,1
        for _ in range(n-1):
            first, second = second, first+second
        return second