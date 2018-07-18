class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0]*n
        ans[0] = 1
        v2,v3,v5 = 2,3,5
        i2,i3,i5 = 1,1,1
        for i in range(1,n):
            ans[i] = min(v2,v3,v5)
            if ans[i] == v2:
                v2 = ans[i2]*2
                i2 +=1
            if ans[i] == v3:
                v3 = ans[i3]*3
                i3 +=1
            if ans[i] == v5:
                v5 = ans[i5]*5
                i5 +=1
        return ans[-1]

print(Solution().nthUglyNumber(10))