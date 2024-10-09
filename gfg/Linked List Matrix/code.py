#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        if not mat: return none
        
        n = len(mat)
        nodes = [[None for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                nodes[i][j] = Node(mat[i][j])
        for i in range(n):
            for j in range(n):
                if j + 1 <  n:
                    nodes[i][j].right = nodes[i][j+1]
                if i + 1 <  n:
                    nodes[i][j].down = nodes[i+1][j]

        return nodes[0][0]
        
