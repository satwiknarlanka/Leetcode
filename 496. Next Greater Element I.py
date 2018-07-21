class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lenNums2 = len(nums2)
        address = dict(zip(nums2,[i for i in range(lenNums2)]))
        ans = []
        for x in nums1:
            val = -1
            for gt in range(address[x],lenNums2):
                if nums2[gt]>x:
                    val = nums2[gt]
                    break
            ans.append(val)
        return ans
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution().nextGreaterElement(nums1,nums2))