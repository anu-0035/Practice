class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Brute force
        # num = ""
        # for c in s:
        #     num += str(ord(c) - ord("a") + 1 )
        # for i in range(k):
        #     x = 0
        #     for c in num:
        #         x += int(c)
        #     num = str(x)
        # return int(num)
        def convert(s):
            return ''.join(str(ord(c) - ord('a') + 1) for c in s)
        
        def transform(n):
            return sum(int(d) for d in str(n))
        
        num = convert(s)
       
        for _ in range(k):
            num = transform(num)
        
        return num

        
