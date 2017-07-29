class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = x ^ y
        d = 0
        while r > 0:
            d += r % 2
            r = r >> 1
        # return bin(x ^ y).count('1')
        return d
        

s = Solution()
# print(0b11)
print(s.hammingDistance(0xffffffff, 0x7fffffff))
