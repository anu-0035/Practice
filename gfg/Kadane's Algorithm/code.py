#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        max_so_far = max_ending_here = arr[0]
        for i in range(1,len(arr)):
            max_ending_here = max(arr[i],arr[i]+ max_ending_here)
            max_so_far = max(max_ending_here,max_so_far)
        return max_so_far

