class Solution(object):
    def distinctDifferenceArray(self, nums):
        diff = []

        for i in range(len(nums)):
            prefix_set = set(nums[:i+1])
            suffix_set = set(nums[i+1:])
            diff.append(len(prefix_set) - len(suffix_set))
        
        return diff
