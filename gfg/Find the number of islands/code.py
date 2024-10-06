class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        n, m = len(grid), len(grid[0])
        
        def dfs(i, j):
            # Check for out of bounds and if the cell is water
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return
            
            # Mark the cell as visited by sinking the island
            grid[i][j] = 0
            
            # Explore all eight possible directions
            directions = [
                (1, 0), (0, 1), (-1, 0), (0, -1),
                (1, 1), (-1, -1), (1, -1), (-1, 1)
            ]
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # Found an island
                    island_count += 1
                    dfs(i, j)  # Sink the island
        
        return island_count
