#code
size= int(input())
for i in range(size):
    N,marks = map(int,input().split())
    arr = list(map(int,input().split()))
    count = 0
    for mark in arr:
        if mark > marks:
            count += 1
    print(count)

