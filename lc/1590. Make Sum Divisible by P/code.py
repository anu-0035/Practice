class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums)
        remain = x % p
        res = 0
        if remain == 0 :
            return res
        
        res = len(nums)
        cur_sum = 0
        remain_to_idx = {0:-1}

        for i,n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - remain + p) % p
            if prefix in remain_to_idx :
                length = i - remain_to_idx[prefix] 
                res = min(res,length)
            remain_to_idx[cur_sum] = i
        
        return -1 if res == len(nums) else res
        
        
