class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictMap = {}
        for index, value in enumerate(nums):
            if target - value in dictMap:
                return dictMap[target - value], index
            else:
                dictMap[value] = index


s = Solution()
print("TestCase:")
print(s.twoSum([2, 7, 11, 15], 9))