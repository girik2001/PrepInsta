'''
INPUT:
Two integers denoting lower limit and upper limit

OUTPUT:
All the numbers in the range that are armstrong numbers
'''
def checkArmstrong(n):
    temp=n
    armstrong=0
    l=len(str(n))
    while temp>0:
        armstrong=armstrong+int((temp%10)**l)
        temp//=10
    if armstrong==n:
        return True

a,b=map(int,input().strip().split())
for i in range(a,b+1):
    arm=checkArmstrong(i)
    if arm:
        print(i,end=" ")