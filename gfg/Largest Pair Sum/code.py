
from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        x,y = arr[0],arr[1]
        for i in range(2,len(arr)):
            if arr[i] > x:
                t = x
                x = arr[i]
                if t > y:
                    y = t
                    
            elif  arr[i] > y:
                t = y 
                y = arr[i]
                if t > x:
                    x = y
        return x+y
