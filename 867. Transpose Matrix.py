class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for j in range(len(A[0])):
            ans.append([A[i][j] for i in range(len(A))])
        return ans

s= Solution()
A= [[1,2,3],[4,5,6]]
print(s.transpose(A))
# easy list(zip(*A))