class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # if dividend == 0:
        #     return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign=1
        quotient=0
        if (dividend<0) ^ (divisor<0):
            sign=(-1)
        dividend=abs(dividend)
        divisor=abs(divisor)
        # while dividend>=divisor:
        #     dividend-=divisor
        #     quotient+=1

        # bits topic solution of TLE
        
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                quotient |= (1 << i)
        return quotient* sign
        