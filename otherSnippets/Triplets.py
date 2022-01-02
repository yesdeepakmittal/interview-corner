''''
Find triplets in an array such that i<j<k and a[i]<a[j]<a[k]

Brute Force - TC - O(N3) | SC - O(1)
'''
arr = [4,1,2,6,9,7,8,4,3]

cnt = 0
for i in range(len(arr)-2):
    for j in range(i+1,len(arr)-1):
        for k in range(j+1,len(arr)):
            if arr[i] < arr[j] and arr[j] < arr[k]:
                cnt += 1

print(cnt)

'Optimized  - TC - O(N2) | SC - O(1)'
if __name__ == "__main__":
	# Your code goes here
	arr = [4,1,2,6,9,7,8,4,3]
	pair = 0
	def left_count(i,arr):
		cnt = 0
		for x in range(0,i):
			if arr[x] < arr[i]:
				cnt += 1
		return cnt
	def right_count(i,arr):
		cnt = 0
		for x in range(i+1,len(arr)):
			if arr[x] > arr[i]:
				cnt += 1
		return cnt
	for i in range(1,len(arr)-1):
		left = left_count(i,arr)
		right = right_count(i,arr)
		pair += left*right
	print(pair)