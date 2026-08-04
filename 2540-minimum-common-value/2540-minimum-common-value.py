class Solution(object):
    def getCommon(self, nums1, nums2):
        d = {}

        for i in nums1:
            d[i] = 1

        for i in nums2:
            if i in d:
                return i

        return -1