def isprime(k):
    if(k==2 or k==3):
        return k
    elif(k%2!=0 and k%3!=0):
        return k
   

numbers=str(input())
list=[]
newlist=[]
numbers=numbers.split()
for i in range(len(numbers)):
    k=int(numbers[i])
    t=isprime(k)
    if(t!=None):
        list.append(t)

print(" Prime numbers:", end="")
for x in list:
    print(x, end=" ")