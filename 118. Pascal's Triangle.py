class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        prev = [1]
        ans = [[1]]
        for i in range(1,numRows):
            curr = prev + [1]
            for j in range(len(prev)-1):
                curr[j+1] = prev[j] + prev[j+1]
            prev = curr
            ans.append(curr)
        return ans

print(Solution().generate(5))