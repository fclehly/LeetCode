class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        begin, end = -1, -1
        l, r = 0, len(nums) - 1
        while l <= r:
            k = (l + r) // 2
            if nums[k] == target:
                begin = end = k
                while begin > 0 and nums[begin - 1] == target:
                    begin -= 1
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                return [begin, end]
            elif nums[k] > target:
                r = k - 1
            else:
                l = k + 1
        return [-1, -1]


solution = Solution()
print(solution.searchRange([2, 8], 8))
