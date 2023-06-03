'''
Find the number from the array which is immediate and nearest smaller to the number x.
'''
arr = [10, 20, 40, 30, 50]

x = 32

nearest_smaller = float('-inf')

for ele in arr:
    if ele < x:
        nearest_smaller = max(nearest_smaller, ele)