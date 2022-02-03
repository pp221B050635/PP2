n=int(input())
z=str(input())
if z=="b":
    res=n*1024
    print(res)
elif z=="k":
    c=int(input())
    res=n/1024
    res=float(res)
    print(round(res, c))