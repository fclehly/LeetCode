import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = '^' + p + '$'
        if re.match(pattern, s) == None:
            return False
        return True

s = Solution()
print(s.isMatch('aab', 'a*'))