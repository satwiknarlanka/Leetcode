class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        actual = (n* (n+1))//2
        return actual - sum(nums)