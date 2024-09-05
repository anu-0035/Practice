
class Solution:
    def nthStair(self, n: int) -> int:
        # The number of distinct ways is (n // 2) + 1
        return (n // 2) + 1
