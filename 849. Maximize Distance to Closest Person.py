import math
def endIndex(arr,val):
    for i in range(len(arr)-1,-1,-1):
        if val == arr[i]:
            return i
    return None

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        start = 0
        end = len(seats)-1
        maxInit = 0
        if not seats[0] or not seats[-1]:
            start = seats.index(1)
            end = endIndex(seats,1)
            if end is None: end = len(seats)-1
            maxInit = max(start,len(seats)-1-end)
        counting = False
        count = 0
        maxCount = 0
        for i in range(start,end):
            if seats[i]:
                if counting:
                    counting = False
                    maxCount = max(maxCount,count)
                    count = 0
            else:
                counting = True
                count += 1
        maxCount = max(maxCount,count)
        return max(math.ceil(maxCount/2),maxInit)
print(Solution().maxDistToClosest([1,0,0,0]))
print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))
print(Solution().maxDistToClosest([1,0]))
print(Solution().maxDistToClosest([0,1]))
print(Solution().maxDistToClosest([1,0,0,1]))
