class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        nRow, nCol = len(matrix), len(matrix[0])
        firstRow = firstCol = False
        for i in range(0, nRow):
            if matrix[i][0] == 0:
                firstCol = True
        for j in range(0, nCol):
            if matrix[0][j] == 0:
                firstRow = True
            
        for i in range(0, nRow):
            for j in range(1, nCol):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, nRow):
            if matrix[i][0] == 0:
                for j in range(0, nCol):
                    matrix[i][j] = 0
        for i in range(1, nCol):
            if matrix[0][i] == 0:
                for j in range(0, nRow):
                    matrix[j][i] = 0
        
        if firstRow:
            for i in range(0, nCol):
                matrix[0][i] = 0
        if firstCol:
            for i in range(0, nRow):
                matrix[i][0] = 0
        
s = Solution()
matrix = [[1, 0]]
s.setZeroes(matrix)
print(matrix)
