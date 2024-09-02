class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        a = sum(chalk)
        if k % a == 0 : return 0
        left = k % a
        for i in range(len(chalk)):
            left -= chalk[i]
            if left < 0:
                return i
