class Solution(object):
    def smallestPalindrome(self, s):
        count = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        left = ""
        middle = ""

        for k, v in sorted(count.items()):
            left += k * (v // 2)

            if v % 2 == 1:
                middle = k

        return left + middle + left[::-1]