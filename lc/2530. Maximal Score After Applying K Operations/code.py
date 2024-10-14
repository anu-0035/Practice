class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        total_score = 0 
        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            total_score += max_val
            heapq.heappush(max_heap,-math.ceil(max_val/3))
        return total_score

        
