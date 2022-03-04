from math import tan, pi
sides=int(input())
lenght=int(input())
def area(sides,lenght):
    e=tan(180/4)
    print(e)
    d=lenght/(2*tan(180/sides))
    print(d)
    return (sides*lenght*d)/2

print(area(sides, lenght))