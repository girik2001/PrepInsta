'''
INPUT:
Any Number

OUTPUT:
Reverse of that number

LOGIC:
take last digit and try to reverse it 
'''

n=int(input())
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)