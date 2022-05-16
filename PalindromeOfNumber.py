'''
INPUT:
Any Integer

OUTPUT:
If the number and reverse of it are equal:
    then print palindrome
else:
    print not palindrome
'''

n=int(input())
temp=n
rev=0
while temp>0:
    rev=rev*10+temp%10
    temp//=10
if rev==n:
    print("Palindrome")
else:
    print("Not a Palindrome")