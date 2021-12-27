class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    
    def LCM(self, A, B):
        def gcd(a,b):
            if a == 0:
                return b 
            else:
                return gcd(b%a,a)
        return A*B//gcd(A,B)
print(Solution().LCM(6,9))