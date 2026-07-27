class Solution(object):
    def maxProduct(self, n):
        a = [int(i) for i in str(n)]
        a.sort()
        return max(a[-1]*a[-2], a[0]*a[1])
        