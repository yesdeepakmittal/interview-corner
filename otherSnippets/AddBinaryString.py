class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
		return bin(int(A,base=2)+int(B,base=2))[2:]

print(Solution().addBinary('101','10'))