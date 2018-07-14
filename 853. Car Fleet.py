class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position)<2:
            return len(position)
        cars = list(zip(position,speed))
        cars = sorted(cars,key=lambda t : t[0])
        time = [float(target - x[0])/x[1] for x in cars]
        result = 1
        head = time.pop()
        while time:
            follower = time.pop()
            if follower>head:
                result += 1
                head = follower
        return result


#test
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

s = Solution()
print(s.carFleet(target, position, speed))