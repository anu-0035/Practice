class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        n = len(arr)
        if n <= 1:
            return -1
        maxsum = -1
        
        for i in range(n-1):
            first = min(arr[i],arr[i+1])
            second = max(arr[i],arr[i+1])
            maxsum = max(maxsum,first+second)
        return maxsum
