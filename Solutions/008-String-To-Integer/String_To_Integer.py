class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ans = 0
        s = ''
        l = 0
        if str == '' or len(str) < 1:
            return 0
        start = 0
        for i in range(0, len(str)):
            if str[i] == ' ' or str[i] == '\t':
                start += 1
            else:
                break
        for i in range(start, len(str)):
            if str[i] == '-' and l < 1:
                s += str[i]
                l += 1
            elif str[i] == '+' and l < 1:
                l += 1
                continue
            elif str[i] >= '0' and str[i] <= '9':
                s += str[i]
                l += 1
            else:
                break
        if s == '' or s == '-' or s == '+':
            return 0
        ans = int(s)
        if ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        elif ans < -2 ** 31:
            ans = -2 ** 31
        return ans


s = Solution()
print(s.myAtoi('1267890'))
print(s.myAtoi('-1234890'))
print(s.myAtoi('1234ass5890'))
print(s.myAtoi('bdf1234890'))
print(s.myAtoi('001.234890'))
print(s.myAtoi('   9 5'))
print(s.myAtoi(''))
print(s.myAtoi('-'))
print(s.myAtoi('+-2'))
