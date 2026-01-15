class Solution(object):
    def semiOrderedPermutation(self, nums):
        n, i, j = len(nums), 0, 0
        while i < n and j < n:
            if nums[i] == 1 and nums[j] != n:
                j += 1
            elif nums[i] != 1 and nums[j] == n:
                i += 1
            elif nums[i] != 1 and nums[j] != n:
                i += 1
                j += 1
            elif nums[i] == 1 and nums[j] == n:
                if i > j:
                    return i + n - j - 2
                return i + n - j - 1
                
        
