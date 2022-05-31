class Solution:
	def search(self,arr,target):
		idx = self.binary_search(arr,target)
		return idx
	
	def binary_search(self,arr,target):
		start = 0
		end = len(arr) - 1
		

		while start <= end:
			mid = (start + end) >> 1
			if arr[mid] > target:
				end = mid - 1
			elif arr[mid] < target:
				start = mid + 1
			else:
				return mid
		return -1

arr = [1,2,3,4,5,6,11,31,33,34,45]
target = 343
print(Solution().search(arr,target))