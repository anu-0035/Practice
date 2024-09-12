class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = len(words)
        for word in words:
            for c in word:
                if c not in allowed :
                    ans -= 1
                    break
        return ans
        
