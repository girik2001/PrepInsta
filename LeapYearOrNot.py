'''
Input:
Year in integer format

Output:

1984
if it is divisible by 4, it is leap year

2000
if it is divisible by 100, it is leap year

1900
but not all divisible by 100's are leap year, hence if it is divisible by 400 it is leap year

hence
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print Leap Year
else:
    print Not Leap Year
'''

year=int(input())
print('Leap Year' if ( (year%4==0 and year%100!=0) or (year%400==0) ) else "Not Leap Year")