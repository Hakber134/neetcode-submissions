class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ClosetoOpenMap = { ")":"(", "]":"[", "}":"{" }

        for char in s: 
            if char in ClosetoOpenMap:
                if stack and stack[-1] == ClosetoOpenMap[char]:
                    stack.pop()
                else:
                    return False
        
            else:
                stack.append(char)

        return True if not stack else False