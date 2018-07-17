class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<2:
            return False
        ans = 1
        for i in range(2,int(num**0.5)+1):
            if not num%i:
                ans = ans+ i+ num/i
        return num == ans

print(Solution().checkPerfectNumber(28))