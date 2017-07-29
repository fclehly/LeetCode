class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor > dividend:
            return 0
        if divisor == 1:
            return dividend
        return 1
        
s = Solution()
print(s.divide(20, 4))
print(1 << 32)