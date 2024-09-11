class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #return bin(start ^ goal)[2:].count("1")
        c = 0
        while start or goal:
            if start%2 != goal%2:
                c+=1
            start = start//2
            goal = goal//2
        return c
