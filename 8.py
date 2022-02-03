from re import I


s=str(input())
t=str(input())
m=0
n=0
for i in range(len(s)):
    if(s[i]==t):
        m=i
        break
    else:
     m=-1
     
     
for i in range(len(s)):
    if(s[-i-1]==t  and len(s)-i-1!=0):
        n=len(s)-i-1
        break
if(m<0):
    print("")
elif(m==n):
    print(m)
elif(m!=n):
    print(m,n)
