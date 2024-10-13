class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minheap = []
        cur_max = float("-inf")
        for i in range(len(nums)):
            heapq.heappush(minheap,(nums[i][0],i,0))
            cur_max= max(cur_max,nums[i][0])
        smallest_range = [float("-inf"),float("inf")]

        while minheap:
            cur_min,row,idx = heapq.heappop(minheap)

            if cur_max - cur_min < smallest_range[1] - smallest_range[0]:
                smallest_range = [cur_min,cur_max]
            
            if idx+1 < len(nums[row]):
                next_val = nums[row][idx+1]
                heapq.heappush(minheap,(nums[row][idx+1],row,idx+1))
                cur_max= max(cur_max,next_val)
            else:
                break
        return smallest_range
        
