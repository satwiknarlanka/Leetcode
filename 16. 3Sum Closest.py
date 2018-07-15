class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n<=3:
            return sum(nums)
        cur = (nums[0],nums[1],nums[2])
        diff = abs(target - sum(cur))
        for i in range(3,n):
            x = []
            x.append((cur[0],cur[1],nums[i]))
            x.append((cur[0],nums[i],cur[2]))
            x.append((nums[i],cur[1],cur[2]))
            x.append(cur)
            diff = [abs(target - sum(x[0])),abs(target - sum(x[1])),abs(target - sum(x[2])),abs(target - sum(cur))]
            cur = x[diff.index(min(diff))]
            if not min(diff):
                break
        return sum(cur)


# Test case
nums = [1,2,4,8,16,32,64,128]
target = 82
s = Solution()
print(s.threeSumClosest(nums,target))