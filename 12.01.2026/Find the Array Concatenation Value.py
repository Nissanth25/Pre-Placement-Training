class Solution(object):
    def findTheArrayConcVal(self, nums):
        sm=0
        i=0
        j=len(nums)-1
        if len(nums)%2!=0:sm+=nums[(i+j)//2]
        while i<j:
            sm+=int(str(nums[i])+str(nums[j]))
            i+=1
            j-=1
        return sm

        
