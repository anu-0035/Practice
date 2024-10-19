
class Solution:
    def roundToNearest (self, s) : 
        #Complete the function
        last = s[-1]
        if last <= "5":
            return s[:-1]+"0"
        s = s[:-1] + "0"
        n = len(s)
        i = -2
        while i>= -n and s[i] =="9":
            s = s[:i] + "0" + s[i+1:]
            i -= 1
        if i < -n:
            return "1" + s
        return s[:i] + str(int(s[i])+1)+s[i+1:]
