class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for letter in s:
            if letter == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif letter == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif letter == ']':
                if not stack or stack.pop() != '[':
                    return False
            else:
                stack.append(letter)
        return not stack