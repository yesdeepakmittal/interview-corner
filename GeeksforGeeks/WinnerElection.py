#code
size = int(input())
votes = []
for i in range(size):
    arr_size = int(input())
    temp = input().split()
    d = {}
    for ele in temp:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    idx = []
    mx = max(list(d.values()))
    for key,value in d.items():
        if value == mx:
            idx.append(key)
    print(sorted(idx)[0])