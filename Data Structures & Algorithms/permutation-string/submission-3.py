class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        map1 = Counter(s1)
        map2 = Counter()

        l = 0
        n = len(s1)
        for r in range(len(s2)):
            map2[s2[r]] += 1
            if (r-l+1) > n:
                map2[s2[l]] -= 1
                l+=1
            
            if map1 == map2:
                return True
        return False