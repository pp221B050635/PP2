n=int(input())
ar=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==0:
            ar[i][j]=j
        elif j==0:
            ar[i][j]=i
        elif i==j:
            ar[i][j]=i*j
        else:
            ar[i][j]=0
for row in ar:
    print(' '.join([str(elem)for elem in row]))