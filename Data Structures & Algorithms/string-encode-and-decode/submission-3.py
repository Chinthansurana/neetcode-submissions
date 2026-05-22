class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for ele in strs:
            res += str(len(ele))+ '#' + ele
        return res

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        while i < len(s):
            j = s.index('#', i)
            ln = int(s[i:j])
            res.append(s[j+1:j+ln+1])
            i = j+ln+1
        return res