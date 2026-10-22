class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n

        def sumOfSquares(x) -> int:
            res = 0
            while x:
                digit = x % 10
                res += (digit*digit)
                x //= 10
            return res

        while True:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False