class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        reverse = 0
        original = x

        while x>0:
            temp = x%10
            reverse = reverse*10 + temp
            x = x//10
        
        return original == reverse
        '''
        # simple solution with string
        return str(x) == str(x)[::-1]
        '''
# test case
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(500))