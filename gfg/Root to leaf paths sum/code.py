# Your task is to complete this function
# function should return max sum level in the tree
class Solution:
    def treePathSum(self,root):
        # Code here
        return self.dfs(root,0)
    def dfs(self,node,cur_sum):
        if not node:
            return 0
        cur_sum = cur_sum * 10 + node.data
        if not node.left and not node.right:
            return cur_sum
        return self.dfs(node.left,cur_sum) + self.dfs(node.right,cur_sum)
