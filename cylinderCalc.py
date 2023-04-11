"""
Script to calculate cylinder area given height and diameter
Author: Kelechi K

"""
#variables length, diameter
# formula for area of cylinder: 2π(d/2)^2 + 2π(d/2)h

PI: float = 3.142

print ("enter diameter: ")
user_input = input()
diameter = float(user_input)

print ("enter height: ")
user_input = input()
height = float(user_input)

#auxiliary variables: radius, raised
radius = diameter/2
raised = radius ** 2
TwoPI: float = 2 * PI

#intermediate variables: Area
Area = TwoPI * raised + TwoPI * radius * height
print(round (Area, 2))
