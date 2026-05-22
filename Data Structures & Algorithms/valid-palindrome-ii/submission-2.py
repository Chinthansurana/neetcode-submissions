class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid(l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                return (is_valid(l+1, r) or is_valid(l, r-1))
            l+=1
            r-=1
        return True
