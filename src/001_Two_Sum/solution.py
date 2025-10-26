class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup_dict = {}
        for i in range(len(nums)):
            if (target-nums[i]) in lookup_dict:
                return [i,lookup_dict[(target-nums[i])]]
            else:
                lookup_dict[nums[i]] = i