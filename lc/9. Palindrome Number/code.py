class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = str(x)
        # return str(x) == str(x)[::-1]
        if x < 0:
            return False
        a,t = 0,x
        while t:
            a = a*10 + t % 10
            t //= 10
        return a == x
        
