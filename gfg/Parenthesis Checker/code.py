class Solution:
    
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the expression
        for char in x:
            # If it's an opening bracket, push onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If it's a closing bracket
            elif char in bracket_map.keys():
                # Check if stack is empty or top of stack doesn't match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                # Pop the top of the stack
                stack.pop()
        
        # If the stack is empty, all brackets were matched; otherwise, not balanced
        return len(stack) == 0

