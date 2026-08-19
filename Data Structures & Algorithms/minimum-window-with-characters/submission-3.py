class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t

        res = ""
        freq = Counter(t)
        l = 0
        have, need = 0, len(freq)
        smap = defaultdict(int)
        res = float('inf')
        reslen = [-1, -1]

        for r in range(len(s)):
            ele = s[r]
            smap[ele] += 1
            if ele in freq and smap[ele] == freq[ele]:
                have += 1
            
            while have == need:
                if (r-l+1) < res:
                    res = r-l+1
                    reslen = [l, r]
                
                smap[s[l]] -= 1
                if s[l] in freq and smap[s[l]] < freq[s[l]]:
                    have -= 1
                l += 1
        l,r = reslen
        return s[l:r+1] if res != float('inf') else ""
            
