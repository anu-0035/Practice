class Solution:
    def reverse(self, x: int) -> int:
        # rev = int(str(abs(x))[::-1])
        # return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        a = 0
        while x:
            a = a*10 + x % 10 
            x //= 10
        if a < -2**31   or a > 2**31 -1:
            return 0
        return a * sign
        
        
        
