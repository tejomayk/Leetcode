class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for index, item in enumerate(nums):
            complement = target-item
            if complement in lookup:
                return [index,lookup[complement]]
            else:
                lookup[item] = index