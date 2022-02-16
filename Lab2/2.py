n=int(input())
s=str(input())
sar=s.split()
con=0
con1=0
con2=0
for i in range(n):
    if con < int(sar[i]):
        con=int(sar[i])
        con1=i
for i in range(n):
    if con2 < int(sar[i]) and con1!=i:
        con2=int(sar[i])
print(con*con2)

