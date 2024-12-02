class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        c = 1
        for w in sentence.split():
            if w.startswith(searchWord):
                return c
            c += 1
        return -1
        
