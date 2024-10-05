class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        window_size = len(s1)

        for i in range(window_size):
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s2) - window_size):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[i]) - ord('a')] -= 1
            s2_count[ord(s2[i + window_size]) - ord('a')] += 1

        return s1_count == s2_count

