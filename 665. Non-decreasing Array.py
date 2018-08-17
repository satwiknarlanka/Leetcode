class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if i==1 or nums[i-2]<=nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                break
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return False
        return True

print(Solution().checkPossibility([1,3,2,3]))
print(Solution().checkPossibility([1,4,2,3]))
print(Solution().checkPossibility([2,3,3,2,4]))