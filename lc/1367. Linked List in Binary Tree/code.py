
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Main function that checks for the downward path
        if not root:
            return False
        
        # Check if the current path starting from root matches the linked list
        if self.dfs(head, root):
            return True
        
        # Recursively check for subpaths starting from the left and right children
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def dfs(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # If the linked list is completely traversed, return True
        if not head:
            return True
        
        # If the tree is empty or values don't match, return False
        if not root or root.val != head.val:
            return False
        
        # Recursively check both left and right child nodes to continue the path
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
