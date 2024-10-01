class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        reminder_count = [0] * k
        for num in arr:
            reminder = num % k
            if reminder < 0:
                reminder += k
            reminder_count[reminder] += 1
        if reminder_count[0] % 2 != 0:
            return False
        for i in range(1,k//2 +1):
            if reminder_count[i] != reminder_count[k - i]:
                return False
        return True

