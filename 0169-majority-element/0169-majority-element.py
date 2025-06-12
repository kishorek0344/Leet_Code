from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        return Counter(nums).most_common(1)[0][0]

        