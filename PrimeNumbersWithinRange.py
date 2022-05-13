'''
Input:
a,b are two integer ranges

Output:
From a to b, check if the number is prime
if it is prime:
    print number
'''
def checkPrime(n):
    if n<2:
        return False
    elif n==2 or n==3:
        return True
    else:
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                return False
        return True

a,b=map(int,input().strip().split())
for i in range(a,b+1):
    if checkPrime(i):
        print(i,end=" ")