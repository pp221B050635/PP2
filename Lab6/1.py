n=int(input())
arr=list()
for i in range(n):
    x=int(input())
    arr.append(x)
def multiplicity(array):
    first=1
    for i in array:
        first*=i
    return first

print(multiplicity(arr))
