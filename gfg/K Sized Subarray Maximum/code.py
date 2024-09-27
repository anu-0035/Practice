#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        ans = []
        dq = deque()
        for i in range(len(arr)):
            if dq and dq[0] < i-k+1:
                dq.popleft()
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                ans.append(arr[dq[0]])
            
        return ans
        
        #code here
