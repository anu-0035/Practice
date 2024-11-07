#User function Template for python3
class Solution:
    # Function to determine if array arr can be split into three equal sum sets.
    def findSplit(self, arr):
        #cod here
        tot = sum(arr)
        i,n = 0,len(arr)
        first,second = -1,-1
        fail = [-1,-1]
        
        cur = 0
        while i < n:
            cur += arr[i]
            if (cur * 3 == tot):
                first = i
                i += 1
                break
            elif cur * 3 > tot:
                return fail
            else:
                i += 1
        
        cur = 0
        while i < n:
            cur += arr[i]
            if (cur * 3 == tot):
                second = i
                i += 1
                break
            elif cur * 3 > tot:
                return fail
            else:
                i += 1
        
        cur = 0
        while i < n:
            cur += arr[i]
            i += 1
        if (cur * 3 == tot):
            return [first,second]
                
        else :
            return fail
