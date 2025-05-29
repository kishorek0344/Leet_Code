class Solution(object):

    def isPalindrome(self, x):
        c=[]
        x=list(str(x))
        i =len(x)-1
        if x <0:
            return False
        while (i>=0):
            c.append(x[i])
            i=i-1
        if x==c:
            print("palindrome")
            return True
        else:
            print("no palindrome")
            return False
        

