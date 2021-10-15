n = input()
k = int(input())

l = []
last = ''
if k>0:
    first = n[:-k]
    for i in n[-k:]:
        l.append(i)

    for i in l:
        last += i

    print(int(last+first))

else:
    first = n[abs(k):]
    for i in n[:abs(k)]:
        last += i
    
    print(int(first+last))