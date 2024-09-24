#User function Template for python3
from collections import Counter

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        p_count = Counter(p)
        required = len(p_count)
        formed = 0
        
        left,right = 0,0
        min_length = float("inf")
        min_left = 0
        
        window_counts = {}
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char,0 ) + 1
            
            if char in p_count and window_counts[char] == p_count[char]:
                formed += 1
        
            while left <= right and formed == required:
                char  = s[left]
                if right - left + 1 < min_length:
                    min_length = right - left +1
                    min_left = left
                    
                window_counts[char] -= 1
                if char in p_count and window_counts[char] < p_count[char]:
                    formed -= 1
                
                left += 1
            right += 1
                

        if min_length == float('inf'):
            return -1
        return s[min_left:min_left + min_length]
        
