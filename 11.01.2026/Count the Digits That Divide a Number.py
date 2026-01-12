class Solution(object):
    def countDigits(self, num):
        str_num, count = str(num), 0
        for digit in str_num:
            if num % int(digit) == 0:
                count += 1
        return count
