def fn():
    k=int(input())
    list.append(k)
    if(k>0):
       return fn()
    else:
        return(k)
list=[]
list2=[]
k=0
list.append(fn())
list.pop(int(len(list))-1)
list.pop(int(len(list))-1)
if(int(len(list))%2==0):
    n=int((int(len(list)))/2)
    for i in range(n):
        k=int(list[i])+int(list[-i-1])
        list2.append(k)
else:
    for i in range(int(len(list))):
        if(i!=int(((int(len(list))-1)/2)+1)):
            k=int(list[i])+int(list[-i-1])
            list2.append(k)
        else:
            k=int(list[i])
            list2.append(k)
            break
for x in list2:
    print(x, end=" ")