class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['']* min(len(s),numRows)
        cur_row = 0
        going_down = False

        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            
            cur_row += 1 if going_down else -1
        
        return "".join(rows)


        
