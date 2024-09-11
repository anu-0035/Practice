#User function Template for python3
import heapq
from typing import List 
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        heapq.heapify(arr) 
        total = 0
        while len(arr) > 1:
            first,second = heapq.heappop(arr),heapq.heappop(arr)
            cost = first + second
            total += cost
            heapq.heappush(arr,cost)
        return total 
    
