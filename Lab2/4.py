n=int(input())
a=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if n%2==0:
            if j<=i:
                a[i][j]='#'
            else:
                a[i][j]='.'
        elif n%2==1:
            if i+j<(n-1):
                a[i][j]='.'
            else:
                a[i][j]='#'
for row in a:
    print("".join([str(elem) for elem in row]))