class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split()
        ans = []
        for word in sentence:
            for item in dict:
                if item == word[:len(item)]:
                    word = item
            ans.append(word)
        return ' '.join(ans)

dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dict,sentence))