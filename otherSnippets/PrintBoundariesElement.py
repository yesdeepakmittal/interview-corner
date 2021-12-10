'''
Print elements which are at boundaries in clock-wise

o/p = 1,6,11,16,21,22,23,24,25,20,15,10,5,4,3,2
'''
a = [[1,6,11,16,21],
     [2,7,12,17,22],
     [3,8,13,18,23],
     [4,9,14,19,24],
     [5,10,15,20,25]]

i = 0
j = 0
for x in range(len(a)-1):
     print(a[i][j],end=' ')
     j += 1
for x in range(len(a)-1):
     print(a[i][j],end=' ')
     i += 1
for x in range(len(a)-1):
     print(a[i][j],end=' ')
     j -= 1
for x in range(len(a)-1):
     print(a[i][j],end=' ')
     i -= 1
