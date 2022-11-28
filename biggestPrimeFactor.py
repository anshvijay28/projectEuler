while True:   
    num = int(input("Enter a number: "))
    if num == 0:
        break

    primeFactors = []

    def isPrime(x):
        for i in range(2, x):
            if (x%i == 0):
                return False
        return True

    def BPF(number):
        if (isPrime(number)):
            primeFactors.append(number)
            return primeFactors
        else:
            for i in reversed(range(2,number)):
                if (number%i==0) and (isPrime(i)):
                    primeFactors.append(i)
                    return BPF(number/i)

    print(BPF(num))




        
    



