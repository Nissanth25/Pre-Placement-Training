class Solution:
    def maximumValue(self, strs):
        mcount = 0
        for i in strs:
            if i.isalpha():
                mcount = max(mcount, len(i))
            elif i.isdigit():
                mcount = max(mcount, int(i))
            else:
                mcount = max(mcount, len(i))
        return mcount
