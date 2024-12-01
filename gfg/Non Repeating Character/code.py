#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        for c in s:
            if freq[c] == 1:
                return c
        return -1
