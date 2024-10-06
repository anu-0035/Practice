class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1,r2,r3 = set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")
        res = []
        for w in words:
            lower_word = w.lower() 
            if lower_word[0] in r1:
                valid_row = r1
            elif lower_word[0] in r2:
                valid_row = r2
            elif lower_word[0] in r3:
                valid_row = r3
            else:
                continue
            if all(char in valid_row for char in lower_word):
                res.append(w)
        return res
