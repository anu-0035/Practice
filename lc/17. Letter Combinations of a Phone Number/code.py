class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        if not digits: return []
        ans = []

        def backtrack(idx,cur):
            if len(cur) == len(digits):
                ans.append(cur)
                return
            letters = phone_map[digits[idx]]
            for l in letters:
                backtrack(idx+1,cur+l)
        backtrack(0,"")
        return ans
        
