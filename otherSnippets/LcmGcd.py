class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def gcd(self,a,b):
        if a == 0:
            return b 
        else:
            return self.gcd(b%a,a)

    def LCM(self, A, B):
        return A*B // self.gcd(A,B)
print('LCM',Solution().LCM(6,9))



## Gcd of more than 2 numbers
arr = [20,40,60,100]
val = 0

for i in arr:
    val = Solution().gcd(val,i)
print('GCD',val)