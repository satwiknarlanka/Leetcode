class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dynamic programming fibonacci series pattern
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a + b
        return b

print(Solution().climbStairs(21))