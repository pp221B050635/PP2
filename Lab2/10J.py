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
passwords=[]
for i in range(n):
    x=str(input())
    passwords.append(x)
for i in range(n):
    if  my_check(passwords[i])==True:
        cnt+=1 
print(cnt)
for i in range(n):
    if  my_check(passwords[i])==True:
        print(passwords[i], end='\n')
