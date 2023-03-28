# Name: Hyunsuk Lee
# SBUID: 114673323

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   temperature = float(input("Please enter temperature in farernheit:"))
   celsius = (temperature - 32) * 5/9
   print("Temperature in celsius:", celsius)
   


def what_to_wear(celsius):
   celsius = int(input("celsius:"))
   if celsius > 20:
        print('You have to wear T-shirts')
   elif 10 < celsius <20:
        print('You have to wear light jacket')
   elif 0 <= celsius < 10:
       print('You have to wear sweater')
   elif -10 <= celsius < 0:
       print('You have to wear Scarf')
   elif -10 > celsius:
       print('You have to wear puffy jacket')
       

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  
import math

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs((x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1))
    return area

     
def euclidean_distance(x1, y1, x2, y2):
    p1 = (x1,y1)
    p2 = (x2,y2)
    sqrs = (p1 [0]- p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
    d = math. sqrt(sqrs)
    return d

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    p = ((((x1-x2)**2)+((y1-y2)**2))**(1/2))+((((x3-x2)**2)+((y3-y2)**2))**(1/2))+((((x1-x3)**2)+((y1-y3)**2))**(1/2))
    return p


# ---------------------------- Exercise III -------------------------------------
# -----------------      -----------------------
# TODO: Fill the functions degrad, apothem  and polygon_area 

import math
def degrad(deg):
    r = deg*(math.pi/180)
    return r

def apothem(number_sides, length_side):
   apo = length_side / (2 * math.tan(180/number_sides))
   return apo

def polygon_area(number_sides, length_side):
   number_sides = int(input("input number of sides:"))
   length_side = float(input("input the length of sides:"))
   area = number_sides * (length_side ** 2) / (4 * math.tan((math.pi) / number_sides))
   return area


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

