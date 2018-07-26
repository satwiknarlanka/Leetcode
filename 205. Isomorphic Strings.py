class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps = {}
        mapt = {}
        for i in range(len(s)):
            if s[i] in maps:
                if maps[s[i]] != t[i]:return False
            else:
                maps[s[i]] = t[i]
            if t[i] in mapt:
                if mapt[t[i]] != s[i]:return False
            else:
                mapt[t[i]] = s[i]
        return True

print(Solution().isIsomorphic('egg','add'))

'''
return len(set(zip(s, t))) == len(set(s)) == len(set(t))
'''