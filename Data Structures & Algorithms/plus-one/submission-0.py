import math
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        length = len(digits)
        retarray = []
        for i,v in enumerate(digits):
            pow = math.pow(10,length-1-i)#10^(3-1-0)
            curr = pow*v #100*1
            num = num + curr
        num = int(num)+1
        for digit in str(num):
            digit = int(digit) 
            retarray.append(digit)
        return retarray
        