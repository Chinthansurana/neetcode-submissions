class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numset = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in numset:
                numset.remove(s[left])
                left += 1
            res = max(res, right-left+1)
            numset.add(s[right])
        return res