class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        count,mini = 0,float("inf")
        res = 0
        for i in range(n):
            for j in range(n):
                x = abs(matrix[i][j])
                res += x
                mini = min(mini,x)
                if matrix[i][j] <= 0:
                    count += 1
        if count % 2 == 0:
            return res
        return res - 2 * mini
        
