#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        # do Code here
        if not root:
            return None
        self.prev = None
        self.head = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev is None:
                self.head = node
            else:
                node.left = self.prev
                self.prev.right = node
            
            self.prev = node
            
            inorder(node.right)
    
        inorder(root)
        return self.head
