class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # Define mapping from closed to open
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            
            # Push open parentheses to stack
            if c in mapping.values():
                stack.append(c)
            
            # Check that top of stack matches 
            else:
                top = stack[-1] if stack else None
                if top == mapping[c]:
                    stack.pop()
                else:
                    return False        
        return True if not stack else False