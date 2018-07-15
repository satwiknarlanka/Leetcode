class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y)[2:].count('1')

s = Solution()
x = 1
y = 4
print(s.hammingDistance(x,y))