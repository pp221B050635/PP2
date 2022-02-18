rabbits=int()
chickens=int()
def solve(numheads, numlegs):
    if numheads<numlegs:
        rabbits=(numlegs-(numheads*2))/2
        chickens=numheads-rabbits
        print(int(chickens),int(rabbits))
    else:
        print("False")
    

x=int(input())
y=int(input())
res=(solve(x,y))
print(res)