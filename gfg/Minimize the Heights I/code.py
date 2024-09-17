#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        diff = arr[-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k
        for i in range(n-1):
            min_ht = min(smallest,arr[i+1] - k)
            max_ht = max(largest,arr[i] + k)
            
            diff = min(diff,max_ht - min_ht)
        return diff