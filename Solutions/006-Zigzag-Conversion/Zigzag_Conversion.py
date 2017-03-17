class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        ans = ''
        step = 2 * numRows - 2
        ans += s[::step]
        for i in range(1, numRows - 1):
            for j in range(i, len(s), step):
                ans += s[j]
                if j + 2 * (numRows - i) - 2 < len(s):
                    ans += s[j + 2 * (numRows - i) - 2]
        ans += s[numRows - 1::step]
        return ans


s = Solution()
print("Testcase:")
print(s.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
print(s.convert('abc', 2))
print(s.convert('abcd', 2))
print(s.convert('a', 1))
print(s.convert('', 0))