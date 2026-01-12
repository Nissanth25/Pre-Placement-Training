class Solution(object):
    def alternateDigitSum(self, n):
        n= int(str(n)[::-1])
        position= 0
        summation=0
        while n>0:
            digit=n%10
            n//=10
            if position%2==0:
                summation+=digit
                position+=1
            else:
                summation+=(-digit)
                position+=1
        return summation
                
