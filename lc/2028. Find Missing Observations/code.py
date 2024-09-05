class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing = (len(rolls) + n) * mean - sum(rolls)
        if missing <  0 or missing > 6 * n :
             return []
        x = missing // n
        y = missing % n
        if x == 0:
            return []
        a = [x] * n
        for i in range(y):
            a[i] += 1
        return a
