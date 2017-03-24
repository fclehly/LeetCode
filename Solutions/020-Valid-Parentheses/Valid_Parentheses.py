class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif c == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif c == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True

        

s = Solution()
print(s.isValid('[](){([])}[]'))
print(s.isValid('[(])'))
print(s.isValid('())'))
print(s.isValid(''))