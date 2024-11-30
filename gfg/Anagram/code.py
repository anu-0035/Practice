#User function Template for python3
from collections import defaultdict

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        if len(s1) != len(s2):
            return False
        freq = defaultdict(int)
        for c in s1:
            freq[c] += 1
        for c in s2:
            if freq[c] == 0:
                return False
            freq[c] -= 1
        return True
