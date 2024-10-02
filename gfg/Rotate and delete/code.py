class Solution:
    def rotateDelete(self,  arr):
        # code here
        n = len(arr)
        for k in range(1,n//2 + 1):
            arr = [arr[-1]] + arr[:-1]
            del arr[-k]
        return arr[0]
