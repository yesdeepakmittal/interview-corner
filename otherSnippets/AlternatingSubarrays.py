''''
Alternate array - array with alternating 1's and 0's
Correct ex. - [1,0,1,0], [0,1,0,1],[1],[0]
Incorrect ex. - [0,0,1],[0,0,0]
return index array that acts as a centre of 2*b + 1

ex - 
 A = [1, 0, 1, 0, 1]
 B = 1 
 o/p -  [1, 2, 3]

 A = [0, 0, 0, 1, 1, 0, 1]
 B = 0 
 [0, 1, 2, 3, 4, 5, 6]
'''
if __name__ == "__main__":
	# Your code goes here
	arr = [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1 ]
	B= 1
	k = 2*B + 1
	ans = []
	for i in range(k,len(arr)+1):
		arr2 = arr[i-k:i]
		centre_index = ((i-k) + i)//2  #left + right index of array divided by 2

		start = i - k
		end = i - 1
		should_consider = True
		while start < end:
			if arr[start] == arr[end]:
				if arr[start] != arr[start + 1]:
					start += 1
					end -= 1
				else:
					should_consider = False
					break
			else: 
				should_consider = False
				break
		if should_consider:
			ans.append(centre_index)	
	print(ans)