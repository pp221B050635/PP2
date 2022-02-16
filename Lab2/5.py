n=input().split()
arr=[]
xor=int()
if(len(n)==1):
    x=int(input())
else:
    x=n[1]
for i in range(0, int(n[0])):
    arr.append(int(x)+2*i)
for i in range(len(arr)):
    x=arr[i]
    xor^=x
print(xor)