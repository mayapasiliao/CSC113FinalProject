# import turtle
# import math
# # from Probability import probability
# from itertools import cycle
#
# def origin(turtle):
# 	turtle.penup()
# 	turtle.setpos(-0,0)
# 	my_turtle.pendown()
#
# def piesections(letter_probability):
# 	central_angle = (360)*letter_probability
# 	return central_angle
#
# COLORS = cycle(['yellow', 'green', 'red', 'cyan', 'white', 'blue', 'mediumpurple'])
# # sample_dict should be the dictionary returned with the probabilities of the letters
# sample_dict = {
# 	"a": 0.10,
# 	"b": 0.10,
# 	"c": 0.20,
# 	"d": 0.60
# }
#
# my_turtle = turtle.Turtle()
# my_turtle.speed("slowest")
# w = turtle.Screen()
# w.setup(450,650,0,0) #width,height
# w.title ("Pie Chart")
#
# r = 150
# label_r = 155
# origin(my_turtle)
# my_turtle.penup()
# my_turtle.sety(-r)
# my_turtle.pendown()
#
# # i should be n, input from user
# for i in sample_dict:
# 	angle = piesections(sample_dict[i])
# 	print(angle)
# 	my_turtle.fillcolor(next(COLORS))
# 	my_turtle.begin_fill()
# 	my_turtle.circle(r,angle)
# 	position = my_turtle.position()
# 	origin(my_turtle)
# 	my_turtle.end_fill()
# 	my_turtle.setpos(position)

import turtle
from itertools import cycle
import math

#takes you to origin of the circle after each section
def origin(vertex):
    turtle.penup()
    turtle.setpos(vertex)
    turtle.pendown()
#we need to divde this by the total
def piesections(segment):
    area = (360)*segment #central angle
    return area

Rainbow = cycle(['red','orange', 'yellow', 'green', 'blue', 'purple', 'pink'])
All_others = ['gray']
Name_of_segment = ["h","e","l","l","o"," ","b","o","y","All other letters"]
segment = {
	"l": 0.20,
	"e": 0.20,
	"All Other Letters": 0.60
}
#window=w
w = turtle.Screen()
w.setup(450,650) #width,height
w.title ("Pie Chart")

#Creating circle with vertex
r=150
vertex=(-0,0)
origin(vertex)
turtle.dot (7,"black")
turtle.penup()
turtle.sety(-r)
turtle.pendown()

angle_sum=0

for n in segment:
    angle=piesections(segment[n])
    turtle.fillcolor(next(Rainbow))
    turtle.begin_fill()
    turtle.circle(r,angle)
    position = turtle.position()
    origin(vertex)
    turtle.end_fill()
    turtle.setpos(position)
    angle_sum += angle
rest=360-angle_sum
turtle.color(next(Rainbow))
turtle.begin_fill()
turtle.circle(r, rest)
position = turtle.position()
origin(vertex)
turtle.end_fill()
turtle.right(90)
turtle.forward(r*1.33)
turtle.left(90)

for n in segment:
	angle=piesections(segment[n])
	turtle.circle(r*1.33,angle/2)
	turtle.write("%s, %f" % (n, segment[n]), align = "center",font=('Arial',8))
	turtle.circle(r*1.33,angle/2)
