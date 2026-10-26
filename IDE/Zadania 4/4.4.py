import math

def tri_area(a,b,c):
    d=(a + b + c)/2
    area=math.sqrt(d*(d-a)*(d-b)*(d-c))
    return area

a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
area=tri_area(a,b,c)
print("Area of given triangle is: ", area)
