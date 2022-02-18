def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def filter_prime(list1):
    primes=[]
    for i in list1:
        primes=list(lambda i : isprime(i)==True)
        print(primes)

n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
print(filter_prime(arr))