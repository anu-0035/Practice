# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, l1, l2):
        MOD = 10**9 + 7
    
        # Convert the first linked list to a number
        num1 = 0
        temp1 = l1
        while temp1:
            num1 = (num1 * 10 + temp1.data) % MOD
            temp1 = temp1.next
        
        # Convert the second linked list to a number
        num2 = 0
        temp2 = l2
        while temp2:
            num2 = (num2 * 10 + temp2.data) % MOD
            temp2 = temp2.next
        
        # Multiply the two numbers and return the result modulo 10^9 + 7
        return (num1 * num2) % MOD

