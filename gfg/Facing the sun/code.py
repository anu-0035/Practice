#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here\
        x,c = height[0],1
        for i in range(1,len(height)):
            if height[i] > x:
                x = height[i]
                c +=1
        return c
            
