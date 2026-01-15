class Solution(object):
    def minLength(self, s):
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "", 1).replace("CD", "", 1)
        return len(s)

        
