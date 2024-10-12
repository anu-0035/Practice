class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_index = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in required_index:
                return [required_index[complement],i] 
            required_index[n] = i

        
        
