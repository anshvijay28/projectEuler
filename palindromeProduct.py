def isPalindrome(num):
    num = str(num)
    backwards = ""
    a = -1
    for i in range(len(num)):
        backwards += num[a]
        a -= 1
    if (backwards == num):
        return True 
    return False 

list1 = []
list2 = []
products = []
palindomres = []

for i in range(100,1000):
    list1.append(i)
    list2.append(i)

for i in list1:
    for n in list2:
        products.append(i * n)

for i in products:
    if isPalindrome(i):
        palindomres.append(i)

print(max(palindomres))
    