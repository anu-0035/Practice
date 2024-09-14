class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        a = max(nums)
        size,res = 0,0
        for n in nums:
            if n == a:
                size += 1
            else:
                size = 0
            res = max(res,size)
        return res


def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines)
    results = []

    for i in range(num_test_cases):
        nums = json.loads(lines[i])
        
        result = Solution().longestSubarray(nums)
        results.append(str(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)
        
        
