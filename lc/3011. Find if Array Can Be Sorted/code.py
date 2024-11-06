class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        values = nums.copy()
        for i in range(n):
            flag = False
            for j in range(n-i-1):
                if values[j] <= values[j+1]:
                    continue
                if bin(values[j]).count("1") == bin(values[j+1]).count("1"):
                    values[j],values[j+1] = values[j+1],values[j]
                    flag = True
                else:
                    return False
            if not flag:
                break
        return True

        
