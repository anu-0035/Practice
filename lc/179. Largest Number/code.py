from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        
        # Define the custom comparator function
        def compare(x, y):
            return -1 if x + y > y + x else 1
        
        # Sort the array using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Concatenate the sorted strings
        largest_number = ''.join(nums)
        
        # Remove leading zeros (if any)
        return largest_number.lstrip('0') or '0'
