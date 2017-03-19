class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        if s == s[::-1]:
            return True
        return False
        
s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(0))