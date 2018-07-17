class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        mark = [False,False] + [True] * (n-2)
        for i in range(2,int(n**0.5)+1):
            if mark[i]:
                mark[i**2:n:i] = [False] * len(mark[i**2:n:i])
        return sum(mark)

print(Solution().countPrimes(10))