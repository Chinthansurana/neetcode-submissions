class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        s_set = set()

        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            res = max(res, r-l+1)
        return res