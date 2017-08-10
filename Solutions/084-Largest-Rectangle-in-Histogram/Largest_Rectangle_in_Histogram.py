class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        ans = 0
        heights.append(0)
        stack = []
        for i, h in enumerate(heights):
            while len(stack) > 0 and heights[stack[-1]] >= h:
                index = stack.pop()
                w = i
                if len(stack) > 0:
                    w = i - 1 - stack[-1]
                ans = max(ans, w * heights[index])
            stack.append(i)
        return ans

s = Solution()
print(s.largestRectangleArea([2, 1, 4, 5, 1, 3, 3]))