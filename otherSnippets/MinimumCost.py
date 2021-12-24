''''
What is the minimum cost to remove all elements from an array?
Cost of removing an element is the sum of all elements presend in the array at that time

TC - O(NlogN) - sorting complexitys
'''
arr = [9,14,21,7,3,4,26,10]
arr.sort(reverse=True)
s = sum(arr)
cost = 0
for i in arr:
    cost += s
    s -= i

print(cost)
