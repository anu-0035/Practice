#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    #code here
	    if arr[0] == 0: return -1
	    n = len(arr)
	    if n == 1 : return 0
	    max_reach,steps,jump = arr[0],arr[0],1
	    for i in range(1,n):
	        if i == n-1:
	            return jump
	        max_reach = max(max_reach,i+arr[i])
	        steps -= 1
	        if steps == 0:
	            jump += 1
	            if i >= max_reach:
	               return -1
	            steps = max_reach - i
	    return -1
	    
