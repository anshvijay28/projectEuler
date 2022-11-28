numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

number = 1

def isDivisible(num, list):
    for i in list:
        if (num % i != 0):
            return False
    return True 

while True:
    divisible = isDivisible(number, numbers)
    if divisible:
        break
    else:
        number +=1 

print(number)


