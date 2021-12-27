class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ''''TC - 0(log2N)'''
        ans = []
        while A>0:
            ans.append(A%2)
            A //= 2
        return ans.count(1)
    
    def numSetBits2(self,A):
        'TC - O(1)'
        cnt = 0
        while A>0:
            cnt += 1
            A = A&(A-1)
        return cnt

print(Solution().numSetBits(3))
print(Solution().numSetBits2(3))

