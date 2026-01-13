class Solution(object):
    def minNumber(self, nums1, nums2):

        inter=list(set(nums1) & set(nums2))
        if len(inter)==0:
            a=min(nums1)
            b=min(nums2)
            if a==b:
                return a
            else:
                res=min(str(a)+str(b),str(b)+str(a))
                return int(res)
        else:
            res=min(inter)
            return res
