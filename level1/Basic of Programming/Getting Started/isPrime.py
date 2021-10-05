import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True



if __name__ == '__main__':
    t = int(input("Enter number of digits"))
    l = []
    for i in range(t):
        l.append(int(input()))
    
    for i in l:
        if isPrime(i): print('prime')
        else: print('not prime')