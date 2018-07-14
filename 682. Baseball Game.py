class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = 0
        stack = []
        for op in ops:
            if op == '+':
                points = 0
                if len(stack)>=2:
                    points = stack[-1] + stack[-2]
                    stack.append(points)
                elif len(stack) == 1:
                    points = stack[-1]
                    stack.append(points)
                else:
                    points = 0
                ans += points
            elif op == 'D':
                points = stack[-1] *2
                ans += points
                stack.append(points)
            elif op == 'C':
                red = stack[-1]
                ans -= int(red)
                stack.pop()
            else:
                ans += int(op)
                stack.append(int(op))
        return ans

s = Solution()

print(s.calPoints(["5","2","C","D","+"]))