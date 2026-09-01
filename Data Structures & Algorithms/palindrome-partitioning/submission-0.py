class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def _is_palin(subs):
            return subs == subs[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                ele = s[start:i+1]
                if _is_palin(ele):
                    path.append(ele)
                    backtrack(i+1, path)
                    path.pop()
        backtrack(0, [])
        return res
