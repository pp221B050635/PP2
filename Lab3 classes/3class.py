class Shape (object):
    def __init__(self):
        pass

    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

x=int(input())
y=int(input())
result=Rectangle(x,y)
print(result.area())