class Solution:
    def isValidSudoku(board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        row = defaultdict(set)
        sq = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell == '.':
                    continue

                if(cell in row[r] or cell in cols[c] or cell in sq[(r//3, c//3)]):

                    return False
                else:
                    row[r].add(cell)
                    cols[c].add(cell)
                    sq[(r//3, c//3)].add(cell)

        return True

    with open('user.out', 'w') as f:
        for case in map(loads, stdin):
            f.write(f'{str(isValidSudoku(case)).lower()}\n')
    exit()
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = [set() for _ in range(9)]
#         cols = [set() for _ in range(9)]
#         subgrid = [set() for _ in range(9)]

#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j] 
#                 if num == ".":
#                     continue
#                 if num in rows[i]:
#                     return False
#                 rows[i].add(num)

#                 if num in cols[j]:
#                     return False
#                 cols[j].add(num)
                
#                 idx = (i // 3) * 3 + (j // 3)
#                 if num in subgrid[idx]:
#                     return False
#                 subgrid[idx].add(num)
        
#         return True

        
