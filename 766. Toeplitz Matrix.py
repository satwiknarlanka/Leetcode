class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """    
        m = len(matrix)
        if m < 2:
            return True
        n = len(matrix[0])
        if n == 1:
            return True
        for x in range(1,m):
            for y in range(1,n):
                if(matrix[x][y] != matrix[x-1][y-1]):
                    return False
        return True

    
#test case
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
s= Solution()
print(s.isToeplitzMatrix(matrix))