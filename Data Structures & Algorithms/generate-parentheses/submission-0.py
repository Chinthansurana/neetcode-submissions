class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, opencnt, closecnt):
            if len(path) == 2*n:
                res.append(''.join(path))
                return 
            
            if opencnt < n:
                path.append("(")
                backtrack(path, opencnt+1, closecnt)
                path.pop()
            if closecnt < opencnt:
                path.append(")")
                backtrack(path, opencnt, closecnt+1)
                path.pop()
        backtrack([], 0, 0)
        return res
