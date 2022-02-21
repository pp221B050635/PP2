def my_check(string):
    lettersu=bool()
    lettersl=bool()
    digits=bool()
    for i in range(len(string)):
        if int(ord(string[i]))>=65 and int(ord(string[i]))<=90:
            lettersu=True
    for i in range(len(string)):
        if int(ord(string[i]))>=97 and int(ord(string[i]))<=122:
            lettersl=True
    for i in range(len(string)):
        if int(ord(string[i]))>=48 and int(ord(string[i]))<=57:
            digits=True
    if digits==True and lettersu==True and lettersl==True:
        return True
    else:
        return False


cnt=0
n=int(input())
new=[]
new1=[]
passwords=[]
for i in range(n):
    x=str(input())
    passwords.append(x)
for i in range(n):
    if  my_check(passwords[i])==True:
        new.append(passwords[i])

new=set(new)
for x in new:
    if x not in new1:
        new1.append(x)
new1.sort
cnt=len(new1)
print(cnt)
for x in new1:
    print(x,'\n')

