class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left,right+1):
            if selfDividing(i):
                ans.append(i)
        return ans
    
def selfDividing(num):
    x = num
    while x//10:
        i = x %10
        if not i or num%i:
            return False
        x = x//10
    return not num%x

print(Solution().selfDividingNumbers(1,22))