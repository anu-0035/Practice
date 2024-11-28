#User function template for Python
class Solution:
    def myAtoi(self, s):
        digits = "0987654321"
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = 1
        s = s.strip()
        
        if not s : return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        a = "" 
        for c in s:
            if c in digits:
                a += c
            else:
                break
        a = int(a) if a else 0
        if a < INT_MIN or a > INT_MAX:
            return INT_MAX if sign == 1 else INT_MIN
        return a * sign
        
