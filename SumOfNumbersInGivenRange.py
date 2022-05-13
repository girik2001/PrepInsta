'''
Input:
Starting Number, Ending Number

Formula to find sum of N natural numbers:
n*(n+1)/2

Output:
Sum of range
'''

a,b=map(int,input().strip().split())
print(f'{int((b*(b+1)/2)-(a*(a+1)/2)+a)}')