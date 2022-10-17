n = int(input('Enter a decimal number :'))
L=[]
while n!=0:
    temp= n%8
    L.append(temp)
    n = n//8

L.reverse()
for e in L:
    print(e,end='')   