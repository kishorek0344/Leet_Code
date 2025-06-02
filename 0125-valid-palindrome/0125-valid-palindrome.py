class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        res=''
        i=len(s)-1
        while(i>=0):
            res = res+s[i]
            i=i-1
        if (res == s):
            return True
        else:
            return False
        