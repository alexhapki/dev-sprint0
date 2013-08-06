from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

#Define function for writing L. "vertical_size" indicates height of the long vertical line of the L.
def write_l(vertical_size, horizontal_size):
	rt(bob)
	fd(bob, vertical_size)
	lt(bob)
	fd(bob, horizontal_size)

#move bob to left of screen
pu(bob)
bk(bob, 75)
pd(bob)

#H
lt(bob)
fd(bob, 25)
bk(bob, 50)
fd(bob, 25)
rt(bob)
fd(bob, 25)
lt(bob)
fd(bob, 25)
bk(bob, 50)

#jump bob to next letter
pu(bob)
rt(bob)
fd(bob, 10)
pd(bob)

#E
fd(bob, 25)
bk(bob, 25)
lt(bob)
fd(bob, 25)
rt(bob)
fd(bob, 25)
bk(bob, 25)
lt(bob)
fd(bob, 25)
rt(bob)
fd(bob, 25)

#jump bob to next letter
pu(bob)
fd(bob, 10)
pd(bob)

#L
write_l(50, 25)

#jump bob to next letter
pu(bob)
lt(bob)
fd(bob, 50)
rt(bob)
fd(bob, 10)
pd(bob)

#L
write_l(50, 25)

#jump bob to next letter
pu(bob)
fd(bob, 10)
pd(bob)

#O
for i in range(2):
	fd(bob, 25)
	lt(bob)
	fd(bob, 50)
	lt(bob)



wait_for_user()








