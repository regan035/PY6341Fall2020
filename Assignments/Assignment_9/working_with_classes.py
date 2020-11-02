# Gen Li
# 1060038
# Sunday, November 01, 2020 at 11:59 pm
# MSITM 6341

# Assignment #9
# Assignment Title :Working with classes

class Quadrilaterals:
   def __init__(self,name,base,height):
       self.name = name
       self.base = base
       self.height = height

   def CalculateArea(self):
        return (self.base+self.height)/2

class Trapezoid(Quadrilaterals):
    def __init__(self,name,base,height):
        super().__init__(name, base, height)

    # Override CalculationArea in parent class
    def CalculateArea(self):
        return((self.base+self.height)/2)*self.height

class Rectangle(Quadrilaterals):
    def __init__(self, name, base, height):
        super().__init__(name, base, height)

    # Override CalculationArea in parent class
    def CalculateArea(self):
        return self.base * self.height

#Create new instances for Trapezoid and Rectangle classes
t1 = Trapezoid('Trapezoid1',20,40)
t2 = Trapezoid('Trapezoid2',2,4)

r1 = Rectangle('Rectangle1',20,40)
r2 = Rectangle('Rectangle2',2,4)
r3 = Rectangle('Rectangle3',5.5,9.5)

print()
print(f'The area of {t1.name} is {float(t1.CalculateArea())}')
print(f'The area of {t2.name} is {float(t2.CalculateArea())}')
print(f'The area of {r1.name} is {float(r1.CalculateArea())}')
print(f'The area of {r2.name} is {float(r2.CalculateArea())}')
print(f'The area of {r3.name} is {float(r3.CalculateArea())}')
print()