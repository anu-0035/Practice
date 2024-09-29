
class Solution:
    def count(self,x,k):
        if x % k == 0 :
            return int(x//k)
        return int(x//k) + 1
    def totalCount(self, k, arr):
        # code here
        x = 0
        for i in arr:
            x += self.count(i,k)
        return x
            
