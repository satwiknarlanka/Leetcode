class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            row.reverse()
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return A

s = Solution()
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s.flipAndInvertImage(A))