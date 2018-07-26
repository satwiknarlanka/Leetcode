class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        for x in nums:
            ans ^= x
        return ans^1