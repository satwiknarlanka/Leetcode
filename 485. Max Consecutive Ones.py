class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0
        for i in nums:
            if i == 0:
                ans = max(ans,count)
                count = 0
            else:
                count += 1
        return max(ans,count)

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))