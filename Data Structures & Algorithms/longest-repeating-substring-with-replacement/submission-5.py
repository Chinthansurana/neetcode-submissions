class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        max_val = 0
        l = 0
        res = 0

        for r in range(len(s)):
            freqMap[s[r]] += 1
            max_val = max(max_val, freqMap[s[r]])

            while (r-l+1) - max_val > k:
                freqMap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res