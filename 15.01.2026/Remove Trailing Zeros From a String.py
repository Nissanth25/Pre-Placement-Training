class Solution(object):
    def removeTrailingZeros(self, num):
        num = num.replace("0"," ")
        num = num.strip()
        num = num.replace(" ","0")
        return num
