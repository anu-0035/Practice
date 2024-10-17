class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float("inf")

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right :
                cur_sum = nums[i] + nums[left ]+ nums[right]
                if cur_sum == target:
                    return cur_sum
                
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                
                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
        
