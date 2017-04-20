class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        temp = []
        def dfs(t, l):
            if t == 0:
                ans.append(''.join(temp))
            else:
                if l > 0:
                    temp.append('(')
                    dfs(t - 1, l - 1)
                    temp.pop()
                if t - l > l:
                    temp.append(')')
                    dfs(t - 1, l)
                    temp.pop()
        dfs(n * 2, n)
        return ans


s = Solution()
print(s.generateParenthesis(3))