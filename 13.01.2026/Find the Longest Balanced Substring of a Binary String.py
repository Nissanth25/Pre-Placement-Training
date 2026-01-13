class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        maxlength = 0
        i = 0
        while len(s) > i:
            zerocount = onecount = 0
            while len(s) > i and s[i] == "0":
                zerocount += 1
                i += 1
            while len(s) > i and s[i] == "1":
                onecount += 1
                i += 1
            maxlength = max(maxlength, 2 * min(zerocount, onecount))
        return maxlength
