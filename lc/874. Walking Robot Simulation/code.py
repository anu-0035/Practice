class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Direction vectors for North, East, South, and West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0  # Start facing North
        
        x, y = 0, 0  # Start at origin
        max_distance_squared = 0
        
        # Convert obstacles to a set for fast lookup
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            else:  # Move forward
                for _ in range(command):
                    next_x = x + directions[direction_index][0]
                    next_y = y + directions[direction_index][1]
                    
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_distance_squared = max(max_distance_squared, x*x + y*y)
                    else:
                        break  # Stop moving in this direction if an obstacle is encountered
        
        return max_distance_squared
