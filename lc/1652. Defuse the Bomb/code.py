class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        l = 0
        cur_sum = 0
        for r in range(n + abs(n)):
            cur_sum += code[r % n]
            if r - l + 1 >  abs(k):
                cur_sum -= code[l % n]
                l = (l+1) % n
            if r - l + 1 == abs(k):
                if k > 0:
                    ans[(l -1) % n] = cur_sum
                elif k < 0:
                    ans[(r+1) % n] = cur_sum
        return ans
        
