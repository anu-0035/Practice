#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    
    def missingNumber(self, n, arr):
        total = sum(arr)
        x = (n * (n+1))/2
        return int(x - total)
