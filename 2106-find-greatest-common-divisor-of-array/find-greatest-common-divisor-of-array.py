class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=nums[0]
        b=nums[-1]
        while a!=0 and b!=0:
            if a>=b:
                a=a%b
            else:
                b=b%a 
        if a==0:
            gcd=b
        else:
            gcd=a 
        return gcd