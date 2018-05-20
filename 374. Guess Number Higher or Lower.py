# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
pick = 6
def guess(num):
    if num < pick:
        return 1
    if num > pick:
        return -1
    if num == pick:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min = 0
        max = n
        while True:
            piv = min + (max - min)//2
            x = guess(piv)
            if x == 0:
                return piv
            if x == 1 :
                min = piv +1
            if x == -1:
                max = piv -1


# Test case 
s = Solution()
ans = s.guessNumber(10)
print(ans == pick)