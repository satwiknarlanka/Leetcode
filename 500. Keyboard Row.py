class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for word in words:
            if word[0] in "qwertyuiopQWERTYUIOP":
                should = True
                for c in word:
                    if c not in "qwertyuiopQWERTYUIOP":
                        should = False
                        break
                if should: ans.append(word)
            
            elif word[0] in "asdfghjklASDFGHJKL":
                should = True
                for c in word:
                    if c not in "asdfghjklASDFGHJKL":
                        should = False
                        break
                if should: ans.append(word)
            
            else:
                should = True
                for c in word:
                    if c not in "zxcvbnmZXCVBNM":
                        should = False
                        break
                if should: ans.append(word)
        return ans
print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))