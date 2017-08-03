class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        s = set()
        for num in nums:
            if num in s:
                return False
            else:
                s.add(num)
        return True