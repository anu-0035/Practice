class Solution:
    def minChar(self, s):
        #Write your code here
        def LPS(s):
            lps = [0] * len(s)
            length = 0
            i = 1
            while i < len(s):
                if s[i] == s[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps[-1]
        
        rev_s = s[::-1]
        combined = s+ "#" + rev_s 
        lps = LPS(combined)
        return len(s) - lps
