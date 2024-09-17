#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n = len(arr) 
        arr.sort()
        diff = arr[-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k
        for i in range(n-1):
            min_ht = min(smallest,arr[i+1] - k)
            max_ht = max(largest,arr[i] + k)
            if min_ht < 0:
                continue
            
            diff = min(diff,max_ht - min_ht)
        return diff
