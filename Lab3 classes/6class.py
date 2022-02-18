def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

class Mylist():
    pass
    def __init__(self):
       self.values=[]

    def insert(self, i):
        if not i in self.values:
            self.values.append(i)

    def sort(self):
        newlist=list(filter(lambda i: isprime(i)==True, self.values))
        print(newlist)

n=int(input())
a=[]
result=Mylist()
for i in range(n):
    x=int(input())
    result.insert(x)
print(result.sort())