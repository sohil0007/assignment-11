from math import factorial


n = int(input('Enter a number :'))

factorial=1

while n>0:
    factorial=factorial*n
    n-=1

print('factorial is = ',factorial) 