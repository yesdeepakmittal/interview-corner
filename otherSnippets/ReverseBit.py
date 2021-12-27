''''
Reverse the 32 bit unsigned int

3 ->  3221225472(00000000000000000000000000000011 -> 11000000000000000000000000000000)
'''
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        a = bin(A)[2:]
        l = len(a)
        d = 32 - l
        ans = '0'*d + a
        ans = ans[::-1]
        return int(ans,base=2)

print(Solution().reverse(3))