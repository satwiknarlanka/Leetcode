import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = [x for x in nums]
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = [x for x in self.original]
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.nums)
        return self.nums