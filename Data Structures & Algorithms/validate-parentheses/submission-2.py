class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {']': '[', '}':'{', ')': '('}
        stack = []

        for i in s:
            if i in hmap:
                if stack and hmap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
        