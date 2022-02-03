n, f=input().split()
n=int(n)
f=int(f)
def isPrime(n):
    for i in range(2,int(n**0.5)+1):#I check if a number prime by dividing by numbers which less that square root of this given number
        if n%i==0:
            return False
    return True
if n <500 and isPrime(n)==True and f%2==0:
    print("Good job!")
else:
    print("Try next time!")