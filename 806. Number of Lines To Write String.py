class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines,units = 1,0
        for x in S:
            x_units = widths[ord(x)-97]
            if units + x_units<=100:
                units += x_units
            else:
                lines +=1
                units = x_units
        return [lines,units]

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
print(Solution().numberOfLines(widths,"bbbcccdddaaa"))
