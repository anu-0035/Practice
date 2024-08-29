from collections import deque

# Tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Build BST
class BST:
    def __init__(self):
        self.root = None
    
    # Insertion in a BST
    def insert(self, x):
        if not self.root:
            self.root = TreeNode(x)
            print(f"Node {x}: Successfully added to tree.")
            return
        self._insert(self.root, x)

    def _insert(self, root, x):
        if x < root.val:
            if not root.left:
                root.left = TreeNode(x)
                print(f"Node {x}: Successfully added to the left of {root.val}.")
            else:
                self._insert(root.left, x)
        else:
            if not root.right:
                root.right = TreeNode(x)
                print(f"Node {x}: Successfully added to the right of {root.val}.")
            else:
                self._insert(root.right, x)

    # Deletion in a BST
    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, root, x):
        if not root:
            return root
        if x < root.val:
            root.left = self._delete(root.left, x)
        elif x > root.val:
            root.right = self._delete(root.right, x)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.minimum(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root
    
    # Inorder Traversal: left -> root -> right
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)
    
    # Postorder Traversal: left -> right -> root
    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")
        
    # Preorder Traversal: root -> left -> right
    def preorder(self, root):
        if not root:
            return
        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    # Level Order Traversal
    def level_order(self, root):
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
    # Finding the min element in BST       
    def minimum(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr
    
    # Searching
    def search(self, root, x):
        if not root:
            print(f"Node {x} not found in the tree.")
            return None
        if x == root.val:
            print(f"Node {x} found in the tree.")
            return root
        elif x < root.val:
            return self.search(root.left, x)
        else:
            return self.search(root.right, x)

    # Check for valid BST
    def is_valid_bst(self, root, left=-float("inf"), right=float("inf")):
        if not root:
            return True
        if not (left < root.val < right):
            return False
        return (self.is_valid_bst(root.left, left, root.val) and
                self.is_valid_bst(root.right, root.val, right))

    # Height of BST
    def height(self, root):
        if not root:
            return -1
        left_ht = self.height(root.left)
        right_ht = self.height(root.right)
        return max(left_ht, right_ht) + 1


def main():
    # Create a new BST instance
    bst = BST()
    
    # Insert nodes into the BST
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)
    
    # Perform traversals
    print("\nInorder Traversal of BST:")
    print("[", end=" ")
    bst.inorder(bst.root)
    print("]")
    
    print("\nPreorder Traversal of BST:")
    print("[", end=" ")
    bst.preorder(bst.root)
    print("]")
    
    print("\nPostorder Traversal of BST:")
    print("[", end=" ")
    bst.postorder(bst.root)
    print("]")

    print("\nLevel Order Traversal of BST:")
    print("[", end=" ")
    bst.level_order(bst.root)
    print("]")
    
    # Search for a node
    print("\nSearch for node with value 7:")
    bst.search(bst.root, 7)
    
    print("\nSearch for node with value 20:")
    bst.search(bst.root, 20)
    
    # Get the height of the tree
    print(f"\nHeight of the BST: {bst.height(bst.root)}")
    
    # Check if the tree is a valid BST
    print(f"\nIs the tree a valid BST? {bst.is_valid_bst(bst.root)}")
    
    # Delete a node
    print("\nDelete node with value 7:")
    bst.delete(7)
    
    print("\nInorder Traversal after deletion:")
    print("[", end=" ")
    bst.inorder(bst.root)
    print("]")
    
if __name__ == "__main__":
    main()
