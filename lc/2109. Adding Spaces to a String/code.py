class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index, res = 0, []

        for space in spaces:
            res.append(s[index : space])
            index = space
        
        res.append(s[index :])
        return " ".join(res)
