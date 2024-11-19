#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        k = -1
        for i in range(n-2,-1,-1):
            if arr[i] < arr[i+1]:
                k = i
                break
        if k == -1:
            self.reverse(arr,0,n-1)
            return
            
        
        for l in range(n-1,k,-1):
            if arr[l] > arr[k]:
                arr[l],arr[k] = arr[k],arr[l]
                break
        self.reverse(arr,k+1,n-1)
        
    def reverse(self,a,l,r):
        while l < r:
            a[l],a[r] = a[r],a[l]
            l,r = l+1,r-1
        
