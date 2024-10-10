class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        indexed_num = [(v,i) for i,v in enumerate(nums) ]
        indexed_num.sort()
        max_width = 0
        min_index = float("inf")

        for v,i in indexed_num:
            min_index = min(i , min_index)
            max_width = max(max_width,i - min_index)
        
        return max_width
    
    # def maxWidthRamp(self, nums: List[int]) -> int:
    #     stack = []
    #     ans = 0
    #     for i in range(len(nums)):
    #         if not stack  or nums[stack[-1]] > nums[i]:
    #             stack.append(i)

    #     for i in range(len(nums))[::-1]:
    #         while stack and nums[stack[-1]] <= nums[i]:
    #             ans= max(ans,i -stack[-1])
    #             stack.pop()
    #     return ans
