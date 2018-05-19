class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if n < numRows or numRows == 1:
            return s
        ans = [[s[x]] for x in range(numRows)]
        i = numRows-2
        c = numRows
        switch = False
        while c<n:
            ans[i].append(s[c])
            c += 1
            if switch:
                i += 1
                if i == numRows:
                    switch = False
                    i = numRows-2
            else:
                i -= 1
                if i == -1:
                    switch = True
                    i = 1

        act = ''.join(''.join(x) for x in ans)
        return act

#Test case
s = Solution()
zig = "PAYPALISHIRING"
numRows = 3
print(s.convert(zig,numRows))
print('PAHNAPLSIIGYIR' == s.convert(zig,numRows))
numRows = 4
print(s.convert(zig,numRows))
print('PINALSIGYAHRPI' == s.convert(zig,numRows))