'''
Input:
A positive Integer

Output:
if n<2:
    It is neither prime not composite
elif n==2:
    It is a prime number
else:
    first factor is always found on or before root(n)
    hence from 2 to root(n), if n is divisible:
        then it is not a prime number
    else it is a prime number
'''

n=int(input())
if n<2:
    print("Neither Prime Nor Composite")
elif n==2 or n==3:
    print("Prime")
else:
    prime=True
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            prime=False
            break
    print("Prime" if prime else "Not Prime")