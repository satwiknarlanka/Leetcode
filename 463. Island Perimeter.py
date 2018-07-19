class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i,row in enumerate(grid):
            for j,val in enumerate(row):
                if val:
                    ans += 4
                    if i>0 and grid[i-1][j]: ans -= 2
                    if j>0 and grid[i][j-1]: ans -= 2
        return ans
val = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().islandPerimeter(val))