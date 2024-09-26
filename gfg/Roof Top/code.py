#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        max_step = 0 
        cur_step = 0
        for i in range(len(arr)-1):
            if arr[i+1] > arr[i] :
                cur_step += 1
            else:
                max_step = max(max_step,cur_step)
                cur_step = 0
        max_step = max(max_step,cur_step)
        return max_step
