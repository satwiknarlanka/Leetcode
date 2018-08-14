class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if not n: return -1
        l,h = 0,n-1
        while l<=h:
            mean = (l+h)//2
            if target == nums[mean]:
                return mean
            if target<nums[mean]:
                h = mean-1
            else:
                l = mean+1
        return -1

print(Solution().search([2,5],5))