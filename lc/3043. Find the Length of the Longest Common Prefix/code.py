class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1,arr2 = arr2,arr1
        prefix_set = set()
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n //= 10
        res = 0
        for n in arr2:
            while n and n not in prefix_set:
                n = n // 10
            if n in prefix_set:
                res = max(len(str(n)),res)
        return res
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    i = 0
    args = []
    for a in inputs:
        i += 1
        args.append(a)
        if i & 1:
            continue
        print(str(Solution().longestCommonPrefix(*args)).replace(" ", ""), file=f)
        args = []
exit(0)
