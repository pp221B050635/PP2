n=int(input())
z=str(input())
c=int(input())
if z=="b":
    res=n*1024
elif z=="k":
    res=n/1024
    res=float(res)
print(round(res,c))

