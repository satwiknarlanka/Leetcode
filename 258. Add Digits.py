class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num))!=1:
            num = sum([int(x) for x in  str(num)])
        return num

s = Solution()
print(s.addDigits(38))