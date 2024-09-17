# User function Template for Python3

class Solution:
    def maxLength(self, s):
        # code here
        stack = [-1]  # Initialize stack with -1 to handle base case
        max_len = 0  # To keep track of the maximum length of valid parentheses
    
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push the index of the opening parenthesis
            else:
                stack.pop()  # Pop the top (match the closing parenthesis with the last opening one)
                if stack:
                    max_len = max(max_len, i - stack[-1])  # Calculate the length of valid substring
                else:
                    stack.append(i)  # If stack is empty, push the current index
    
        return max_len

