class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        num_set = {}
        res = 0

        for r in range(len(s)):
            while s[r] in num_set and num_set[s[r]] >= l:
                l = num_set[s[r]] + 1
            num_set[s[r]] = r
            res = max(res, r-l+1)
        return res