from isPrime import isPrime

low = int(input('Enter lower limit'))
high = int(input('Enter higher limit'))
l = []

for i in range(low,high+1):
    if isPrime(i): print(i)