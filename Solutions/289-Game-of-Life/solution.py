from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
        rows = len(board)
        cols = len(board[0])
        for i in range(0, rows):
            for j in range(0, cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    row = i + neighbor[0]
                    col = j + neighbor[1]
                    if row >= 0 and row < rows and col >= 0 and col < cols and abs(board[row][col]) == 1:
                        live_neighbors += 1
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2 
                elif board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1

        for i in range(0, rows):
            for j in range(0, cols):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0


if __name__ == '__main__':
    s = Solution()
    a = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]
    s.gameOfLife(a)
    print("----")
    for i in range(0, len(a)):
        print(a[i])
