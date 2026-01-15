class Solution(object):
    def isFascinating(self, n):
        n2 = str(n * 2)
        n3 = str(n * 3)
        n = str(n)
        n += n2 + n3

        if len(n) != 9:
            return False

        if '0' in n:
            return False
            
        required_digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        
        return set(n) == required_digits
