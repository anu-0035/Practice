#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        sum1,sum2,res = 0,0,0
        i,j = 0,0
        while (i < len(arr1) and j < len(arr2) ):
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i +=1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j +=1
            else:
                res += max(sum1,sum2) + arr1[i]
                sum1,sum2 = 0,0
                i,j = i+1,j+1
        sum1 += sum(arr1[i:]) if arr1[i:] else 0
        sum2 += sum(arr2[j:]) if arr2[j:] else 0
        res += max(sum1,sum2)
        return res
                
