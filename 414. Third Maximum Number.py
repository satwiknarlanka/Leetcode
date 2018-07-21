class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums))<3: return max(nums)
        first,mid,last = min(nums),min(nums),min(nums)
        for num in set(nums):
            if num>first:
                last = mid
                mid = first
                first = num
            elif num>mid:
                last = mid
                mid = num
            elif num > last:
                last = num
        return last
print(Solution().thirdMax([2, 2, 3, 1]))