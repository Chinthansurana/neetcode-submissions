class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while mask&b:
            a,b = a^b, (a&b)<<1
        return mask&a if b > 0 else a