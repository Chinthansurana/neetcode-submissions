class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1m = Counter(s1)
        s2m = Counter()

        l = 0
        for r in range(len(s2)):
            s2m[s2[r]] += 1
            if (r-l+1) > len(s1):
                s2m[s2[l]] -= 1
                l += 1
            if s1m == s2m:
                return True
        return False
