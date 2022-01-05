'''
A = 4
********
***  ***
**    **
*      *
*      *
**    **
***  ***
********
'''
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    space = 0
    star = A
    for i in range(A):
        for st in range(star):
            print('*',end='')
        for sp in range(2*space):
            print(' ',end='')
        for st in range(star):
            print('*',end='')
        star -= 1
        space += 1
        print()
    star += 1
    space -= 1
    for i in range(A):
        for st in range(star):
            print('*',end='')
        for sp in range(2*space):
            print(' ',end='')
        for st in range(star):
            print('*',end='')
        star += 1
        space -= 1
        print()

    return 0

if __name__ == '__main__':
    main()