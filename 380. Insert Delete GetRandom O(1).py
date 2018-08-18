import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ans = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ans:
            self.ans[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ans:
            self.nums[self.ans[val]] = self.nums[-1]
            self.ans[self.nums[-1]] = self.ans[val]
            self.nums.pop()
            del self.ans[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()