class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        first_occurance = {}
        max_dist = 0
        for i in range(len(arr)):
            if arr[i] not in first_occurance:
                first_occurance[arr[i]] = i
            else:
                dist = i -  first_occurance[arr[i]]
                max_dist = max(max_dist,dist)
        return max_dist

