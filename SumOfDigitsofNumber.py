'''
INPUT:
Any Integer

OUTPUT:
Sum of Digits

Logic:
take the last digit from number and keep adding
'''

n=int(input())
summ=0
while n>0:
    last=n%10
    summ+=last
    n//=10
print(summ)