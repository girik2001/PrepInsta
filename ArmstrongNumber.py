'''
INPUT:
Any integer

OUPUT:
If sum of digits to power length of integer is equal to the number itself, it is called as Armstrong Number
'''

n=int(input())
temp=n
length=len(str(n))
arm=0
while temp>0:
    last=temp%10
    arm=arm+int(last**length)
    temp//=10
if arm==n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
