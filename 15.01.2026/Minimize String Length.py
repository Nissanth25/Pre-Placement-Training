class Solution(object):
    def minimizedStringLength(self, s):
        l = list(s)
        st = set(l)
        return len(st)
        
