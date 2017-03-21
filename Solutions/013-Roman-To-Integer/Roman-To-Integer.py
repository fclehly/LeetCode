class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        m = {'I':1, 'X':10, 'C':100, 'M':1000, 'V':5, 'L':50, 'D':500}
        if len(s) <= 1:
            return m[s]
        i = 0
        while (i < len(s)):
            x1 = m[s[i]]
            x2 = m[s[i + 1]] if i < len(s) - 1 else 0
            if x1 < x2:
                ans += x2 - x1
                i += 2
            else:
                ans += x1
                i += 1
        return ans

s = Solution()
print(s.romanToInt('DCXXI'))
print(s.romanToInt('M'))
print(s.romanToInt('CM'))
print(s.romanToInt('XX'))

