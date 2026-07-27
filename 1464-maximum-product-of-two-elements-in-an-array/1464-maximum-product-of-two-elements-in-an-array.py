class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)<=2:
            return (nums[0]-1)*(nums[1]-1)
        else:
            return (nums[-1]-1)*(nums[-2]-1)
        