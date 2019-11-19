class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s, result = '1', '1'
        for k in range(2, n + 1):
            count = 0
            t = s[0]
            for i in range(0, len(s)):
                if s[i] == t:
                    count += 1
                else:
                    result += str(count) + s[i]
            s = result
        return result


if __name__ == '__main__':
    solution = Solution()
    a1 = solution.countAndSay(4)
    print(a1)
