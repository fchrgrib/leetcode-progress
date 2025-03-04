class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        i = 0
        if dividend < 0 or divisor <0:
            i=1
        if dividend < 0 and divisor <0:
            i=0
        if abs(dividend) == abs(divisor):
            if i ==0:
                return 1
            else:
                return -1
        sum = dividend//divisor
        if sum >= 2**31-1:
            return 2**31-1
        if sum <= -2**31:
            return -2**31
        if dividend%divisor != 0:
            return sum+i
        return sum
        