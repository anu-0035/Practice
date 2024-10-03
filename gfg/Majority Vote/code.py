class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        if not nums:
            return [-1]
        n = len(nums)
        can1,can2 = None,None
        count1,count2 = 0,0
        
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
            elif count1 == 0:
                can1,count1 = num,1
            elif count2 == 0:
                can2,count2 = num,1
            else:
                count1 -= 1
                count2 -= 1
        
        count1,count2 = 0,0
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
        
        res = []
        
        if count1 > n // 3:
            res.append(can1)
        if count2 > n //3:
            res.append(can2)
        
        return sorted(res) if res else [-1]
