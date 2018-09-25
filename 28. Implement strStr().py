class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        if n == 0 : return 0
        for i in range(len(haystack)-n+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
        return -1

print(Solution().strStr("hello","ll"))
print(Solution().strStr("aaaaa","bba"))
print(Solution().strStr("a","a"))