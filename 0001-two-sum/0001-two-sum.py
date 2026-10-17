class Solution(object):
    def twoSum(self, nums, target):
        mapping = dict()
        for idx in range(len(nums)):
            if nums[idx] in mapping.keys():
                return [mapping[nums[idx]], idx]
            else:
                diff = target - nums[idx]     
                mapping[diff] = idx


