'''
Maximum GCD after removing an element from the array
'''
A = [12,15,18]
n = len(A)

def gcd(x,y):
	if x == 0:
		return y
	else:
		return gcd(y%x,x)

prefix = [0] * n
suffix = [0] * n

prefix[0] = A[0]
for i in range(1,n):
	prefix[i] = gcd(prefix[i-1],A[i])

suffix[n-1] = A[n-1]
for i in range(n-2,-1,-1):
	suffix[i] = gcd(suffix[i+1],A[i])

# print(prefix)
# print(suffix)

mx = 0
for i in range(1,n-1):
	mx = max(mx,gcd(prefix[i-1],suffix[i+1]))
print(mx)