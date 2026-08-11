class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq = 0
        res = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            while (r-l+1) - max_freq > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l+=1
            res = max(res, r-l+1)
        return res