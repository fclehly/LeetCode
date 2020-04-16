from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        records = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if records[int(board[i][j]) - 1] != 0:
                        return False
                    else:
                        records[int(board[i][j]) - 1] = 1
            records = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.':
                    if records[int(board[j][i]) - 1] != 0:
                        return False
                    else:
                        records[int(board[j][i]) - 1] = 1
            records = [0] * 9
        for i in range(3):
            for j in range(3):
                for n in range(3):
                    for m in range(3):
                        if board[i * 3 + n][j * 3 + m] != '.':
                            if records[int(board[i * 3 + n][j * 3 + m]) - 1] != 0:
                                return False
                            else:
                                records[int(board[i * 3 + n][j * 3 + m]) - 1] = 1
                records = [0] * 9
        return True

s = Solution()
a = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
for l in a:
    print(l)
print(s.isValidSudoku(a))