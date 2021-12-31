if __name__ == "__main__":
	# Your code goes here
	#User function Template for python3

	class Solution:
		def sort012(self,arr):
			# TC - O(N)
			zero_cnt = 0
			one_cnt = 0
			two_cnt = 0
			for i in range(len(arr)):
				if arr[i] == 0:
					zero_cnt += 1
				elif arr[i] == 1:
					one_cnt += 1
				else:
					two_cnt += 1
			ans = []
			for i in range(zero_cnt):
				ans.append(0)
			for i in range(one_cnt):
				ans.append(1)
			for i in range(two_cnt):
				ans.append(2)
			return ans
		
		def sort2(self,arr):
			'TC - O(NlogN)'
			arr.sort()
			return arr
	print(Solution().sort012([0,2,1,2,0,2,0,0,1]))
	print(Solution().sort2([0,2,1,2,0,2,0,0,1]))