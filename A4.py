#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Rectangle(Shape):
    pass
class Square(Shape):
    pass
choice='y'
while choice.lower()=='y':
    c=int(input("Enter 1 for rectangle and 2 for square:"))
    if c==1:
        l=float(input("Enter length of rectangle:"))
        b=float(input("Enter breadth of rectangle:"))
        r=Rectangle(l,b)
        print("Area of rectangle= ",r.area())
    elif c==2:
        s=float(input("Enter side of square:"))
        s1=Square(s,s)
        print("Area of Square= ",s1.area())
    else:
        print("Wrong choice")
    choice=input("Do you want to continue y/n:")        
