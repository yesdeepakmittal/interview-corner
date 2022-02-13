'''
find maximum value x such that
- x divides A | A % x = 0
- x & B are coprimes | gcd(B,x) = 1

Approach - 
A = 30/gcd(30,12) -> 30/6 : A = 5 -> gcd(5,12) - 1 
'''

def gcd(x,y):
    'TC - O(logN)'
    if x == 0:
        return y
    else:
        return gcd(y%x,x)

class Solution:
    def ques(self, A, B):
        while gcd(A,B) != 1:
            A = A//gcd(A,B)
        return A

print(Solution().ques(30,12))