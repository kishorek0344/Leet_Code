class Solution(object):
    def reverse(self, x):
        x = str(x)
        a=[]
        i=len(x)-1
        while(i>=0):
            a.append(x[i])
            i=i-1
        result =  ''.join(a)

        if result[-1]=="-":
            result = '-'+result[:-1]
        result = int(result)

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result

