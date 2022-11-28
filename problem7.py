def isPrime(num):
    for i in range(2, num):
        if (num%i == 0):
            return False
    return True 

primes = []
num = 2

while len(primes) < 10001:
    if isPrime(num):
        primes.append(num)
    num += 1


print(primes[-1])
