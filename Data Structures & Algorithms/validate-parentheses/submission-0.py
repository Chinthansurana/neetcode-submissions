class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}': '{', ']': '[', ')': '('}

        for ele in s:
            if ele in closeToOpen:
                if stack and stack[-1] == closeToOpen[ele]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        
        return True if not stack else False
                