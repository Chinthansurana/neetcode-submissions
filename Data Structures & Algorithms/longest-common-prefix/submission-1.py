class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sm, bg = min(strs), max(strs)
        for i in range(len(sm)):
            if sm[i] != bg[i]:
                return sm[:i]
        return sm