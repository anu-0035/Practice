class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n = len(arr)
        i = 0
        while i < n-1:
            if arr[i] != 0 and arr[i] == arr[i+1]:
                arr[i] *= 2
                arr[i+1] = 0
                i += 1
            i += 1
        ans = [n for n in arr if n != 0 ]
        zeros = arr.count(0)
        return ans + [0] * zeros
