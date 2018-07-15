class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        ans = []
        diff = ord('a') - ord('A')
        l = ord('A')
        h = ord('Z')
        for char in str:
            if l<= ord(char) <=h:
                char = chr(ord(char) + diff)
            ans.append(char)
        return ''.join(ans)


s = Solution()
print(s.toLowerCase("Hello"))