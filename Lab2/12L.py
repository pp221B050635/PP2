s=str(input())
cnt=0
for i in range(len(s)):
    if (s[i]=='(' or '{' or '['):
        cnt=cnt+1
    else:
        cnt=cnt-1
        if cnt < 0:
            print('NO')
            
if cnt==0:
    print('YES')
else:
    print('NO')
