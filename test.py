import turtle
import math
# from Probability import probability
from itertools import cycle

def origin(turtle):
	turtle.penup()
	turtle.setpos(-0,0)
	my_turtle.pendown()

def piesections(letter_probability):
	central_angle = (2*math.pi)*letter_probability
	return central_angle

COLORS = cycle(['yellow', 'green', 'red', 'cyan', 'white', 'blue', 'mediumpurple'])
# sample_dict should be the dictionary returned with the probabilities of the letters
sample_dict = {
	"a": 0.50,
	"b": 0.10,
	"c": 0.20,
	"d": 0.60
}

my_turtle = turtle.Turtle()
my_turtle.speed()
w = turtle.Screen()
w.setup(450,650,0,0) #width,height
w.title ("Pie Chart")

# r=150
# my_turtle.circle(r)
# origin(my_turtle)
# my_turtle.forward(150)

r = 150
origin(my_turtle)
my_turtle.penup()
my_turtle.sety(-r)
my_turtle.pendown()

angle_sum = 0
# i should be n, input from user
for i in sample_dict:
	angle = piesections(sample_dict[i])
	my_turtle.fillcolor(next(COLORS))
	my_turtle.begin_fill()
	my_turtle.circle(r,angle)
	position = my_turtle.position()
	origin(my_turtle)
	my_turtle.end_fill()
	my_turtle.setpos(position)
	angle_sum += angle

my_turtle.circle(r, 360-angle_sum)
