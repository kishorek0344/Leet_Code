class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        start = nums[0]
        end = nums[-1]
        res=[]
        for i in range(start,end):
            if i not in nums:
                res.append(i)
        return res

        