class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        n = len(arr)
        a,b = arr[:n//2],arr[n//2:] 
        ans = []
        for i in range(n//2):
            ans.append(b.pop())
            ans.append(a[i])
        if b:
            ans.append(b.pop())
        return ans

