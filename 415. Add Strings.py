from collections import deque
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        if len(num1)> len(num2):
            big = num1
            small = num2
        else:
            big = num2
            small = num1
        l = len(small) -1
        h = len(big) -1 
        ans = deque()
        while l>=0:
            sum = int(small[l]) + int(big[h]) + carry
            if sum>9:
                carry = 1
                sum -= 10
            else:
                carry = 0
            ans.appendleft(str(sum))
            l -= 1
            h -= 1
        
        while h>=0:
            sum = int(big[h]) + carry
            if sum>9:
                carry = 1
                sum -= 10
            else:
                carry = 0
            ans.appendleft(str(sum))
            h -=1
        if carry:
            ans.appendleft(str(carry))
        return ''.join(ans)

s = Solution()
num1 = "408"
num2 = "5"
print(s.addStrings(num1,num2))