class Solution:
    def checkSorted(self, arr):
        #code here
        n = len(arr)
        swapCnt = 0

        for i in range(n):
            if arr[i] == i + 1:
                continue
            
            while arr[i] != i + 1:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
                swapCnt += 1

        if swapCnt == 2 or swapCnt == 0:
            return True
        return False
