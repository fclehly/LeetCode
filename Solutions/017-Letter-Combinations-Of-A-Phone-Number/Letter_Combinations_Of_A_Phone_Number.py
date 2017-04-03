class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        ans = []
        word = []
        m = [' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        def dfs(cur):
            if cur >= len(digits):
                ans.append(''.join(word))
            else:
                for d in m[int(digits[cur])]:
                    word.append(d)
                    dfs(cur + 1)
                    word.pop()
        dfs(0)
        return ans
        

        

s = Solution()
print(s.letterCombinations('2345'))