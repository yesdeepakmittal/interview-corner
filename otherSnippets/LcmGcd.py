from re import S


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


## GCD for a range of numbers
class Solution2:
    # @param A : string
    # @param B : string
    # @return a strings
    def gcd(self,x,y):
        if x == 0:
            return y
        else:
            return self.gcd(y%x,x)
            
    def solve(self, A, B):
        val = 0
        if int(A) > int(B):
            A,B = int(B),int(A)
        for i in range(int(A),int(B)+1):
            val = self.gcd(val,i)
            if val == 1:   
                return 1
        return val

print(Solution2().solve('1234','1111234342'))