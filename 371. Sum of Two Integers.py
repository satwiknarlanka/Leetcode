from ctypes import c_int32
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            a = c_int32(a).value #needed because python doesn't use 32 bit int like c
            b = c_int32(b).value
            a,b = a^b,a&b
            b = b<<1
        return a           

print(Solution().getSum(5,3))