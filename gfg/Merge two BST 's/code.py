class Solution:
    def inorder(self,node,lst):
        if not node:
            return 
        self.inorder(node.left,lst)
        lst.append(node.data)
        self.inorder(node.right,lst)
        
    def merge(self, root1, root2):
        # code here
        l1 = []
        l2 = []
        self.inorder(root1,l1)
        self.inorder(root2,l2)
        
        ans = []
        i,j = 0,0
        while i < len(l1) and j < len(l2):
            if l1[i] > l2[j]:
                ans.append(l2[j])
                j += 1
            else:
                ans.append(l1[i])
                i += 1
        
        
        ans += l1[i:] if i < len(l1) else l2[j:]
        return ans
