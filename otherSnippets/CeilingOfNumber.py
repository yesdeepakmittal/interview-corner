'''
Find the ceiling of a number: number >= target
'''

class Solution:
	def search(self,arr,target):
		return self.ceiling(arr,target)
	
	def ceiling(self,arr,target):
		#if target is greater than maximum of array
		if target > arr[len(arr) - 1]:
			return -1

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
		return start

arr = [1,2,3,4,5,6,7,8,11,12,13,14,23]
target = 10
print(Solution().search(arr,target))  # Output = 8