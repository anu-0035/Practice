#User function Template for python3
from collections import defaultdict
class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        diff_count = defaultdict(int)
        diff_count[0] = 1
        diff = 0
        count = 0
        
        for n in arr:
            if n == x:
                diff += 1
            elif n == y:
                diff -= 1
            count += diff_count[diff] 
            diff_count[diff] += 1
        return count
