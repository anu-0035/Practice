class Solution:
    def search(self, pat: str, txt: str) -> list:
        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = compute_lps(pat)
        indices = []
        i = j = 0
        
        while i < len(txt):
            if pat[j] == txt[i]:
                i += 1
                j += 1
            
            if j == len(pat):
                indices.append(i - j)
                j = lps[j - 1]
            elif i < len(txt) and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return indices
