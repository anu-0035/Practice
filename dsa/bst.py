class Treenode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
    
    def inorder(self,):
        if not root:
            return
        print("Inorder Traversal : [",end = " ")
        self.inorder(root.left)
        print(root.val ,end = " ")
        self.inorder(root.right)
        print("]",end = " ")
        
    def postorder(self,root):
        if not root:
            return
        print("Postorder Traversal : [",end = " ")
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.val ,end = " ")
        print("]",end = " ")
        
    def preorder(self,root):
        if not root: 
            return
        print("Preorder Traversal : [",end = " ")
        print(root.val ,end = " ")
        self.inorder(root.left)
        self.inorder(root.right)
        print("]",end = " ")
    
    def insert(self,x):
        if not self.root :
            self.root = TreeNode(x)
            print("Node {x} : Successfully added to tree. ")
            return
        _insert(self.root,x)

    def _insert(self,root,x):
        if x < root.val:
            if not root.left:
                root.left = TreeNode(x)
            else:
                self._insert(root.left,x)
        else:
            if not root.right:
                root.right = TreeNode(x)
            else:
                self._insert(root.right,x)
            
    def delete(self,x):
        self.root = self._delete(self.root,x)

    def _delete(self,root,x):
        if not root:
            return root
        if x < root.val:
            root.left = self._delete(root.left,x)
        elif x > root.val:
            root.right = self._delete(root.right,x)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.minimum(root.right)
            root.val = temp.val
            root.right = self._delete(root.right,temp.val)
        
    

            
    def minimum(self,root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr
    
    def search(self,root):
        if not root:
            print("Tree is EMPTY!")
            return
        
        
        
    
    
        