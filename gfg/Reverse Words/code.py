# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,s):
        # code here 
        a = s.split(".")
        a.reverse()
        return ".".join(a)
