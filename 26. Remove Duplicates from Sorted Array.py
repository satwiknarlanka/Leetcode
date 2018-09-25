class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ptr = 1
        curr = 0
        if len(nums)<2:
            return len(nums)
        while ptr<len(nums):
            if nums[curr] == nums[ptr]:
                ptr += 1
            else:
                curr +=1
                nums[curr] = nums[ptr]
                ptr +=1
        return curr+1

nums = []
print(Solution().removeDuplicates(nums))
print(nums)