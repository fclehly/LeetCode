class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        a = [0] * n
        res = []
        def isValid(row):
            for i in range(0, row):
                if abs(i - row) == abs(a[i] - a[row]) or a[i] == a[row]:
                    return False
            return True
        def dfs(cur):
            if cur >= n:
                res.append(list(map(lambda x: '.' * x + 'Q' + '.' * (n - x - 1), a)))
            else:
                for i in range(0, n):
                    a[cur] = i
                    if isValid(cur):
                        dfs(cur + 1)
        dfs(0)
        return res

s = Solution()
print(s.solveNQueens(4))
