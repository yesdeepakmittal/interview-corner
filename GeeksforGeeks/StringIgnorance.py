#https://practice.geeksforgeeks.org/problems/string-ignorance/0/
size = int(input())
for i in range(size):
    s = input()
    d = {}
    ans = ''
    for i in s:
        temp = i.lower()
        if temp in d:
            d[temp] += 1
            if d[temp] % 2 != 0:
                ans += i
        else:
            d[temp] = 1
            ans += i
    print(ans)