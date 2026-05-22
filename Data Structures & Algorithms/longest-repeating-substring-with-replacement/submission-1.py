class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        res = 0
        window = {}
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1+window.get(s[r], 0)
            maxf = max(maxf, window[s[r]])
            while (r-l+1) - maxf > k:
                window[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res