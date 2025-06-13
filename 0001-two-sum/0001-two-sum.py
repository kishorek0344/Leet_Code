from itertools import combinations

class Solution(object):
    def twoSum(self, nums, target):
        for (i1, v1), (i2, v2) in combinations(enumerate(nums), 2):
            if v1 + v2 == target:
                return [i1, i2]
