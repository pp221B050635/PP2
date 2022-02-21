def reverce(s):
    k=[]
    for i in range(len(s)):
        k.append(s[-i-1])
    return k

txt=str(input())
list=txt.split()
newlist=(reverce(list))
for x in newlist:
    print(x, end=" ")