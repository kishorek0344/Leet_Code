from itertools import combinations

class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return (hash_map[nums[i]],i)
            hash_map[target - nums[i]] = i