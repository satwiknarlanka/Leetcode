class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0]*n
        ans[0] = 1
        val = [x for x in primes]
        index = [1] * len(primes)
        for i in range(1,n):
            res = min(val)
            ans[i] = res
            minvals = [i for i,x in enumerate(val) if x==res]
            for inc in minvals:
                val[inc] = ans[index[inc]] * primes[inc]
                index[inc] +=1
        return ans[-1]

print(Solution().nthUglyNumber(10))