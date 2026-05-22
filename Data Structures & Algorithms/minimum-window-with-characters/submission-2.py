class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        window, countT = {}, Counter(t)
        have, need = 0, len(countT)
        res, reslen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] = 1+window.get(s[r], 0)
                if window[s[r]] == countT[s[r]]:
                    have+=1
            
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -=1
                l+=1
        return s[res[0]:res[1]+1] if res[0] != -1 else ""
