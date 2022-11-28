squareOfSum = 0
sumOfSquares = 0

for i in range(1,101):
    squareOfSum += i
    i *= i
    sumOfSquares += i



squareOfSum *= squareOfSum

answer =  squareOfSum - sumOfSquares

print(answer)

