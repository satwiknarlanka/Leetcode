class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans += n & 1
            n >>=1
            ans <<=1 
        return ans>>1

s = Solution()
print(s.reverseBits(43261596))
'''
one line solution:
return int(''.join(reversed(bin(n)[2:].zfill(32))),2)
'''