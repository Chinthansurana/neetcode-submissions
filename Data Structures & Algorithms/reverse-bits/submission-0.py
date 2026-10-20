class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_int = 0
        for _ in range(32):
            reversed_int = (reversed_int<<1) | (n&1)
            n >>= 1
        return reversed_int
        