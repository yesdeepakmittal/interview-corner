'''
i/p : A = 2
o/p : [[1,2]
       [4,3]]
'''
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    ans = []
    
    
    k = 1
    for var in range(n//2):
        forward = []
        for temp in range(n):
            forward.append(k)
            k += 1
        ans.append(forward)
        backward = []
        for temp in range(n):
            backward.insert(0,k)
            k += 1
        ans.append(backward)
    if n&1 == 1:
        forward = []
        for temp in range(n):
            forward.append(k)
            k += 1
        ans.append(forward)
    for i in ans:
        for j in i:
            print(j,end=' ')
        print()
    return 0

if __name__ == '__main__':
    main()