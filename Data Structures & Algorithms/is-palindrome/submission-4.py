class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        print(i,j)
        while i < j:
            print(s[i], s[j])
            while i<j and not s[i].isalnum():
                print("i", s[i])
                i += 1
            while i<j and not s[j].isalnum():
                print("j", s[j])
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
