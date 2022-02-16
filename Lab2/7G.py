n=int(input())
demons={}
for i in range(n):
    name, fear=input().split()
    if fear not in demons.keys():
        demons[fear]=0
    demons[fear]+=1
m=int(input())
cnt=[]
for i in range(m):
    name, fear, number=input().split()
    if fear not in demons.keys():
        continue
    if demons[fear]<=int(number):
        demons[fear]=0
    else:
        demons[fear]-=int(number)
print("Demons left: " + str(sum(demons.values())))

