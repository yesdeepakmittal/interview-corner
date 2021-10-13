n = input()
l = list(n)
d = {}
d1 = {}
for index,value in enumerate(n):
    d[index+1] = int(value)

print(d.items())
for i,j in d.items():
    d1[j-1] = i

print(d1.items())

for key,value in d1.items():
    l[key] = value

print(l)