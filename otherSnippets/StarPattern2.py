'''
A = 7
*******
*    *
*   *
*  *
* *
**
*

A = 4
****
* *
**
*
'''
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    star = A 
    space = A - 3
    for i in range(A):
        print('*',end='')
    print()
    for i in range(A-1):
        print('*',end='')
        for sp in range(space):
            print(' ',end='')
        space -= 1
        if i != A-2:
            print('*',end='')
        print()
    return 0

if __name__ == '__main__':
    main()