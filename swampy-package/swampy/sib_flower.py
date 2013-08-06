# Flower excercise (4.2) from Week 0

# Name: Alex Choi


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()
bob.delay = 0.0001

#This function defines a general shape that can be invoked for polygon(), circle(), and arc().
def generalShape(turtleName, length, n, theta):
	for i in range(n):
		fd(turtleName, length)
		lt(turtleName, theta)

#This function defines an arc with the turtle's name, radius of circle, and theta as the fraction of the circle to draw as parameters.
def arc(turtleName, r, theta):
	from math import pi
	fractionToDraw = (2 * r * pi) * theta/360
	n = 60
	arcLength = fractionToDraw/n
	arcAngle = float(theta)/n
	
	generalShape(turtleName, arcLength, n, arcAngle)	#I replaced the length and theta with arcLength and arcAngle

#This function defines one stem of the flower.
def stem(turtleName):
	#This is the part where bob draws the stem.
	arc(bob, 50, 100)
	lt(bob, 79)
	arc(bob, 50, 100)
	#This is the part where bob turns after drawing the stem.
	rt(bob, 20)

#This is for a 7-petaled flower.
stem(bob)
stem(bob)
stem(bob)
stem(bob)
stem(bob)
stem(bob)
stem(bob)



wait_for_user()					

