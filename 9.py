logins=[]
n=int(input())
for i in range(n):
    logins.append(str(input()))
for i in range(n):
    if "@gmail.com" in logins[i]:
        print(logins[i].replace("@gmail.com"," "))