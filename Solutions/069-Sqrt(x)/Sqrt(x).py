class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        l, r = 1, x // 2
        mid = (l + r) // 2
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            elif (mid + 1) * (mid + 1) > x:
                return mid
            else:
                l = mid + 1
        return mid

s = Solution()
# print(s.mySqrt(3))
for i in range(0, 36):
    print(i, s.mySqrt(i))