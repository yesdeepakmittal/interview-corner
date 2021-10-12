n = int(input("Enter number of terms"))
a, b = 0, 1
if n==1: print(a)
elif n==2: print(b)
else:
    print(a)
    print(b)
    for i in range(2,n):
        temp = b
        b = a+b
        print(b)
        a = temp