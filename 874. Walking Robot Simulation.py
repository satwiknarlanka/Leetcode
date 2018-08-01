class Solution:
    def robotSim(self, commands, obstacles):
        i = j = mx = d = 0
        move, obstacles = [(0, 1), (-1, 0), (0, -1), (1, 0), ], set(map(tuple, obstacles))
        for command in commands:
            if command == -2: d = (d + 1) % 4
            elif command == -1: d = (d - 1) % 4
            else:
                x, y = move[d]
                while command and (i + x, j + y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i ** 2 + j ** 2)
        return mx

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
print(Solution().robotSim(commands,obstacles))