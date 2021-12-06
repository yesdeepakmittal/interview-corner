'''
arr = [a,d,g,a,g,a,g,f,g]
count no. of pairs (a,g)

Brute Force
TC - O(N2) | SC - O(1)
'''
arr = ['a','d','g','a','g','a','g','f','g']
cnt = 0
for i in range(len(arr)):
    if arr[i] == 'a':
        for j in range(i+1,len(arr)):
            if arr[j] == 'g':
                cnt += 1
print(cnt)

'''
Using suffix sum
TC - O(N) | SC - O(N)
'''
sf = [0]*len(arr)
for i in range(len(arr)):
    if arr[i] == 'g':
        sf[i] = 1         #Like One hot encoding

for i in range(len(arr)-2,-1,-1):
    sf[i] = sf[i+1] + sf[i]

cnt = 0    
for i in range(len(arr)):
    if arr[i] == 'a':
        cnt += sf[i]
print(cnt)

'''
Carry Forward approach 
TC - O(N) | SC - O(1)
'''
cnt_g = 0
cnt = 0
for i in arr[::-1]:
    if i == 'g':
        cnt_g += 1
    elif i == 'a':
        cnt += cnt_g
print(cnt)
