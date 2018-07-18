class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        if not len(words): return ''
        ans = []
        count = 1
        for word in words:
            if word[0] in ['a','e','i','o','u','A','E','I','O','U']:
                ans.extend(word+'ma' + 'a'*count + ' ')
                count +=1
            else:
                ans.extend(word[1:]+word[0]+'ma' + 'a'*count+' ')
                count +=1
        ans.pop()
        return ''.join(ans)

I = "I speak Goat Latin"
O = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
print(Solution().toGoatLatin(I) == O)