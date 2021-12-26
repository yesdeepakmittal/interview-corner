''''
Number of elements in an array greater than current element is equal to current element
'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
		A.sort(reverse=True)
		if A[0] == 0:
			return 1
		for i in range(1,len(A)):
			if i == A[i] and A[i] != A[i-1]:
				return 1
		return -1

print(Solution().solve([3, 2, 1, 3]))  #2