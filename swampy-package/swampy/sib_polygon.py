# Polygon excercise from Week 0

# Name: ALex Choi

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()
bob.delay = 0.01				

#This function defines a general shape that can be invoked for polygon(), circle(), and arc().
def generalShape(turtleName, length, n, theta):
	for i in range(n):
		fd(turtleName, length)
		lt(turtleName, theta)

#This function defines a square with the turtle's name and length of one side as parameters.
def square(turtleName, length):
	for i in range(4):
		fd(turtleName, length)
		lt (turtleName)

#This function defines a polygon with the turtle's name, length of one polygon side, and number of polygon sides as parameters.
def polygon(turtleName, length, n):
	theta = 360.0 / n
	generalShape(turtleName, length, n, theta)

#This function defines a circle with the turtle's name and radius of the circle.
from math import pi
def circle(turtleName, r):
	circumference = 2 * r * pi
	n = 60						#Anything above 60 for n would draw an incomplete circle. Not quite sure why...
	length = circumference/n
	theta = 360/n
	generalShape(turtleName, length, n, theta)

#This function defines an arc with the turtle's name, radius of circle, and theta as the fraction of the circle to draw as parameters.
def arc(turtleName, r, theta):
	fractionToDraw = (2 * r * pi) * theta/360
	n = 60
	arcLength = fractionToDraw/n
	arcAngle = float(theta)/n
	
	generalShape(turtleName, arcLength, n, arcAngle)	#I replaced the length and theta with arcLength and arcAngle


#This is where I tested out all my functions.
square(bob, 20)
polygon(bob, 50, 6)
circle(bob, 30)
arc(bob, 40, 180)







wait_for_user()					