class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        longs = ""
        for i in range(len(s)):
            oddp = longest(i,i)
            evenp = longest(i,i+1)
            if len(oddp) > len(longs):
                longs = oddp
            if len(evenp) > len(longs):
                longs = evenp
        
        return longs
