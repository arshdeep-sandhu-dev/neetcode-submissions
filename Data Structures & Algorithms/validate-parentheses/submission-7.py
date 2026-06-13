class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={'(': ')', '{': '}', '[':']'}
    
        for op in s:
            if op in d:
                stack.append(op)
            elif op in d.values():
                if not stack or d[stack.pop()]!=op:
                    return False
            else:
                return False
        return len(stack)==0