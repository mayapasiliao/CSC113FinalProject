import turtle
import math
# from Probability import probability

def origin(turtle):
    turtle.penup()
    turtle.setpos(-0,150)
	my_turtle.pendown()

def piesections(letter_probability):
	return central_angle = (2*math.pi)*letter_probability

Name_of_segment = ["h","e","l","l","o"," ","g","u","y","s","All other letters"]
segment = [0.10,0.10,0.20,0.60]
# sample_dict should be the dictionary returned with the probabilities of the letters
sample_dict = {
	"a": 0.10,
	"b": 0.10,
	"c": 0.20,
	"d": 0.60
}

my_turtle = turtle.Turtle()
w = turtle.Screen()
w.setup(450,650,0,0) #width,height
w.title ("Pie Chart")

r=150
my_turtle.circle(r)
origin(my_turtle)
my_turtle.forward(50)

# i should be n, input from user
for i in sample_dict:
	angle = piesections(sample_dict["a"])
	origin(my_turtle)
	my_turtle.right(angle)
	my_turtle.forward(50)
	origin(my_turtle)
