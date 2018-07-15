class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x.lower() for x in s if x.isalnum()]
        return s == s[::-1]

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))