class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # return int(bin(num)[2:].replace('0','1'),2) ^num
        i = 1
        while i<=num:
            i = i<<1
        i = i -1
        return i^num

print(Solution().findComplement(5))