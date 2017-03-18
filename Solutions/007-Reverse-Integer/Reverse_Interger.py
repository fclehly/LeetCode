class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        max = 2 ** 31 - 1
        min = -2 ** 31
        s1 = str(x)
        if s1[0] == '-':
            ans = -int(s1[:0:-1])
        else:
            ans = int(s1[::-1])
        if ans > max or ans < min:
            ans = 0
        return ans
        

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(2147483647))