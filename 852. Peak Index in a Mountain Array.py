class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        prev = A[0]
        for i in range(1,len(A)):
            if prev > A[i]:
                return i-1
            else:
                prev = A[i]

s = Solution()
A = [0,2,1,0]
print(s.peakIndexInMountainArray(A))
# easier solution is return A.index(max(A))