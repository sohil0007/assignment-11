n = int(input('Enter a decimal number :'))
L=[]
while n!=0:
    temp= n%2
    L.append(temp)
    n = n//2

L.reverse()
for e in L:
    print(e,end='')    