class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        count = 0
        cur_sum = 0
        sum_map = {0: 1}

        for n in arr:
            cur_sum += n
            
            
            
            complement = cur_sum - tar
            
            if complement in sum_map:
                count += sum_map[complement]
            
            if cur_sum in sum_map:
                sum_map[cur_sum] += 1
            else:
                sum_map[cur_sum] = 1
        
        return count
