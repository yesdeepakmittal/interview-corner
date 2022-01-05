ans = []
# A = [5, 6, -1, 7, 8]
A = [ 8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ]
arr = []
for i in A:
    if i > 0:
        arr.append(i)
    else:
        if len(arr)> 0:
            ans.append(arr)
        arr = []
if len(arr)>0:
    ans.append(arr)

mx = 0
for i in ans:
    if len(i) > mx:
        mx = len(i)
        a = i
print(a) #[5591744, 4058312, 2210051, 5680315]