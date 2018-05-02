# Divide two integers without using multiplication, division and mod operator.
#If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = 0
        negative = False
        if dividend < 0 or divisor < 0:
            negative = True
        if dividend < 0 and divisor < 0:
            negative = False
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            tempVal, curQuotient = divisor, 1
            while dividend >= tempVal:
                tempVal <<= 1
                curQuotient <<= 1
            quotient += curQuotient >> 1
            dividend -= tempVal >> 1

        if negative:
            quotient = 0 - quotient
        quotient = max(-1*2**31, min(quotient, 2**31-1))
        return quotient

if __name__ == "__main__":
    dividend = int(input().strip())
    divisor = int(input().strip())

    print(Solution().divide(dividend, divisor))
