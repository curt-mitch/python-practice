# draw a circle out of squares

import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_triangle(some_turtle):
	for i in range(1,4):
		some_turtle.forward(100)
		some_turtle.right(120)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	# create the turtle brad from Turtle class
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	for i in range(0,36):
		draw_square(brad)
		brad.right(10)

	window.exitonclick()

draw_art()