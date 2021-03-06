class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numset = set(nums)
        for i in range(len(nums)):
            val = target - nums[i]
            if val in numset:
                j = nums.index(val)
                if i!=j:
                    return [i,j]

print(Solution().twoSum([2, 7, 11, 15],9))