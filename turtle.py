import turtle

sides = int(raw_input('How many sides for this shape? '))
			#ask how long the sides should be
length = int(raw_input('What length should the sides be? '))
print 'Turtle Time!'
			#opens screen
window = turtle.Screen()
			#assigns Shawn as a turtle
Shawn = turtle.Turtle()
		 	#calculation for Shawn's turning
degrees = (180 - (180*(sides-2)/sides))
		 	#for loop for drawing circle
for side in range(sides):
	Shawn.forward(length)
	Shawn.left(degrees)
