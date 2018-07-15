class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # use zip function to get the dict
        morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--','z':'--..'}
        ans = set()
        for word in words:
            code = ""
            for char in word:
                code += morse[char]
            ans.add(code)
        return len(ans)

s = Solution()
words = ["gin", "zen", "gig", "msg"]
print(s.uniqueMorseRepresentations(words))