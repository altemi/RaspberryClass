import sys
year= sys.stdin.readline()
year= int(year)
if (year%4 == 0) & (year%100 !=0) | (year%400 ==0):
    print('1')
else :
    print('0')