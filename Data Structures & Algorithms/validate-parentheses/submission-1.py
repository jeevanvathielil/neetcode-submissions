class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        HashS = {"]" : "[", "}" : "{", ")" : "("}

        for c in s:
            if c in HashS:
                if stack and stack[-1] == HashS[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)

        return True if not stack else False

        
