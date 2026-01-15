class Solution(object):
    def isGood(self, nums):
        a = max(nums)
        arr = []
        for i in range(1,a+1):
            arr.append(i)
        arr.append(a)
        nums.sort()
        return arr == nums
        
