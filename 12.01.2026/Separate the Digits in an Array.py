class Solution(object):
    def separateDigits(self, nums):
        res = []
        for num in nums[::-1]:
            while num:
                res.append(num % 10)
                num //= 10
        return res[::-1]
