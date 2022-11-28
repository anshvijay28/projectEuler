perfectSquares = []
triple = []
cSquared = 0

def isPerfectSquare(num):
    if (num**0.5).is_integer():
        return True
    return False

for a in range(1, 100):
    for b in range(1, 100):
        cSquared = (a**2) + (b**2)
        if isPerfectSquare(cSquared):
            triple.append(a)
            triple.append(b)
            triple.append(cSquared**0.5)
            perfectSquares.append(triple)
        del triple[:]
        cSquared = 0

print(perfectSquares)





