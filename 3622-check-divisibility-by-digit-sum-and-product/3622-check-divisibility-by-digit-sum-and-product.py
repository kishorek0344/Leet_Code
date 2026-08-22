class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        original=n
        sum_=0
        product =1
        while n>0:
            last = n%10
            sum_ =sum_+last
            product=product*last
            n=n//10
        if original%(sum_+product) == 0:
            return True
        else:
            return False
        