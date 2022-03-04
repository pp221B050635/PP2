import math
n=int(input())
m=int(input())
s=str(input())
if(s=='+' or s=='*' or s=='-' or s=='/'):
    if s=='+':
        print(n+m)
    elif s=='*':
        print(n*m)
    elif s=='-':
        print(n-m)
    elif s=='/':
        print(n/m)
else:
    print('False')
