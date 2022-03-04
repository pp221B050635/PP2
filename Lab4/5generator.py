n=int(input())
a=(i**2 for i in range(n)[::-1]) 
for x in a:
    print(x)