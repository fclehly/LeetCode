class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            return 0
        nRow = len(grid)
        nCol = len(grid[0])
        d = [[0 for i in range(0, nCol)] for i in range(0, nRow)]
        d[0][0] = grid[0][0]
        for i in range(1, nRow):
            d[i][0] += d[i - 1][0] + grid[i][0]
        for i in range(1, nCol):
            d[0][i] += d[0][i - 1] + grid[0][i]
        for i in range(1, nRow):
            for j in range(1, nCol):
                d[i][j] += min(d[i][j - 1], d[i - 1][j]) + grid[i][j]
        return d[nRow - 1][nCol - 1]

s = Solution()
path = [[1, 2, 3],[1, 1, 1]]
print(s.minPathSum(path))