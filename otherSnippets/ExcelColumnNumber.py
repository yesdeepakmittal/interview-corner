'''
inp -> AB | op -> 28
inp -> ABCD | op -> 19010
'''

class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
		arr = list(A)
		s = 0
		n = len(arr)
		
		for i in range(1,n+1):
			s += (ord(arr[i-1]) - ord('A') + 1) * 26 ** (n-i)
		return s