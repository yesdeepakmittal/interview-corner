#code
size = int(input())
for i in range(size):
    N, num = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = []
    d = {}
    
    for ele in arr:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    
    for key,value in d.items():
        if value > num:
            ans.append(key)
    if len(ans) > 0:
        ans.sort()
        for ele in ans:
            print(ele,end= ' ')
    else:
        print(-1,end='')
    print()