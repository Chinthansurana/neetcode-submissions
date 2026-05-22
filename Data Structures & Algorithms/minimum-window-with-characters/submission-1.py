class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window, countt = {}, Counter(t)
        have, need = 0, len(countt)
        left = 0
        res, reslen = [-1, -1], float('inf')
        for right in range(len(s)):
            ch = s[right]
            if ch in countt:
                window[ch] = 1 + window.get(ch, 0)
                if countt[ch] == window[ch]:
                    have += 1
            
            while have == need:
                if (right - left + 1) < reslen:
                    res = [left, right]
                    reslen = (right - left + 1)
                if s[left] in countt:
                    window[s[left]] -= 1
                    if window[s[left]] < countt[s[left]]:
                        have -= 1
                left += 1
        return s[res[0]:res[1]+1] if res[0] != -1 else ""