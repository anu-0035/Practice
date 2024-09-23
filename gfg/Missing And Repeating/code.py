#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        repeated,missing,x = -1,-1,0
        n = len(arr)
        count = [0] * (n+1)
        for i in arr:
            count[i] += 1
        for i in range(1,n+1):
            if count[i] == 2:
                repeated = i
                x += 1
            elif count[i] == 0:
                missing = i
                x += 1
            if  x == 2:
                break
            
        return [repeated,missing]

