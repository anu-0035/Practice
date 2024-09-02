import heapq
class Solution:
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
		#Code here
		n = len(grid)
		dir = [(0,1),(1,0),(-1,0),(0,-1)]
		min_cost= [[float("inf")] * n for _ in range(n)]
		min_cost[0][0] = grid[0][0]
		pq = [(grid[0][0],0,0)] #weight,row,col
		
		while pq:
		    cur_cost,i,j = heapq.heappop(pq)
		    if i == n-1 and j == n-1: return cur_cost
		    for di,dj in dir:
		        ni,nj = i+di,j+dj
		        if 0 <= ni < n and 0 <= nj < n:
                    new_cost = cur_cost + grid[ni][nj]
                    if new_cost < min_cost[ni][nj]:
                        min_cost[ni][nj] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj))
        return -1
