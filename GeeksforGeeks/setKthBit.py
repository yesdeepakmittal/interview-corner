#https://practice.geeksforgeeks.org/problems/set-kth-bit3724/1/
class Solution:
	def setKthBit(self, N, K):
		# code here
		return N | 1 << K   