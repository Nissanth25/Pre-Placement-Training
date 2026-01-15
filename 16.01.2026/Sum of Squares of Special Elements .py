class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums)
        res=0
        for i in range(n):
            print(nums[i])
            if n%(i+1)==0:
                res=res+nums[i]*nums[i]
                print(res)

        return res
