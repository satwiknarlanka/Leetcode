def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    n = 0
    for x in nums:
        if x != val:
            nums[n] = x
            n = n+1
    return n

#test case
nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))
print(nums)