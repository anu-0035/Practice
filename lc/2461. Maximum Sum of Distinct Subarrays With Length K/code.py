class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        cur_sum = 0
        prev_idx = {}

        for r in range(len(nums)):
            cur_sum += nums[r]

            i = prev_idx.get(nums[r],-1)

            while l <= i or r - l + 1 > k:
                cur_sum -= nums[l]
                l += 1
            if r-l+1 == k:
                res = max(res,cur_sum)
            prev_idx[nums[r]] = r


        return res



# class Solution:
#     def maximumSubarraySum(self, nums: List[int], k: int) -> int:
#         count = defaultdict(int)
#         res = 0
#         l = 0
#         cur_sum = 0

#         for r in range(len(nums)):
#             cur_sum += nums[r]
#             count[nums[r]] += 1

#             if r - l + 1 > k:
#                 count[nums[l]] -= 1
#                 if count[nums[l]] == 0:
#                     count.pop(nums[l])
#                 cur_sum -= nums[l]
#                 l += 1
            
#             if len(count)== r - l + 1 == k:
#                 res = max(res,cur_sum)


#         return res

