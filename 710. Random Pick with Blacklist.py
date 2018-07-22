from random import randint
class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        blackset = set(blacklist)
        self.map = {}
        index = 0
        maxblack = len(blacklist)
        self.limit = N-len(blacklist)
        blacklist = [x for x in blacklist if x<self.limit]
        for i in range(self.limit,N):
            if i not in blackset:
                self.map[blacklist[index]] = i
                index +=1

    def pick(self):
        """
        :rtype: int
        """
        val = randint(0,self.limit-1)
        return self.map[val] if val in self.map else val


'''
Algo:
Treat the first N - |B| numbers as those we can pick from. 
Iterate through the blacklisted numbers and map each of them to to one of the remaining non-blacklisted |B| numbers

For picking, just pick a random uniform int in 0, N - |B|. If its not blacklisted, return the number. 
If it is, return the number that its mapped to

init with sorting
blacklist = sorted(blacklist)
        blackset = set(blacklist)
        self.map = {}
        index = 0
        maxblack = len(blacklist)
        self.limit = N-len(blacklist)
        for i in range(self.limit,N):
            if i not in blackset:
                self.map[blacklist[index]] = i
                index +=1


The best submission in leetcode is not a correct soution
it doesn't give an equal chance to all numbers.
It just clears all the test cases.
Here is the solution
class Solution:

    def __init__(self, N, blacklist):
        self.forbidden = set(blacklist)
        self.n = N
        self.used = set()
        self.cur = 0
    def pick(self):
        while self.cur in self.forbidden:
            self.cur += 1
        if self.cur < self.n:
            num = self.cur
            self.cur += 1
        else:
            num = self.used.pop()
        self.used.add(num)
        return num
'''

obj = Solution(3, [1])
for i in range(10):
    print(obj.pick())