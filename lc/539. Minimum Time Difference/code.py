class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            total_minutes = h * 60 + m
            minutes.append(total_minutes)

        # Sort the minutes
        minutes.sort()

        # Initialize the minimum difference
        min_diff = float('inf')

        # Calculate the differences between consecutive times
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)

        # Check the difference between the last and the first time (wrap-around)
        wrap_around_diff = (1440 - minutes[-1] + minutes[0])  # 1440 is the total minutes in a day
        min_diff = min(min_diff, wrap_around_diff)

        return min_diff
            
