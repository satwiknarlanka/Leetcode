class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = [x for x in S if x!='-']
        lenS = len(S)
        ans = []
        if lenS<K:
            return ''.join(S).upper()
        ans.extend(S[0:lenS%K])
        for x in range(lenS%K,lenS,K):
            ans.extend('-')
            ans.extend(S[x:x+K])
        ans = ans[1:] if ans[0]=='-' else ans
        return ''.join(ans).upper()

print(Solution().licenseKeyFormatting('2-5g-3-J',2))
