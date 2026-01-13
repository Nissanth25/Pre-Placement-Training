
class Solution(object):
    def splitNum(self, num):
        arr = []

        while num > 0:
            rem = num % 10
            arr.append(rem)
            num = num //10
        arr.sort()
        num1 = ''
        num2 = ''
        i=0
        while i < len(arr):
            num1+=str(arr[i])
            i+=1
            if i < len(arr):
                num2+=str(arr[i])
                i+=1
        return int(num1) + int(num2)
        
        
