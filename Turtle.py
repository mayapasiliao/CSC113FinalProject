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


#Name_of_segment = the letters in the file
#segment = prob_of_letter (has to calculate the remaining letters not called)
Rainbow = cycle(['red','orange', 'yellow', 'light green', 'blue', 'purple', 'pink'])
All_others = ['gray']
Name_of_segment = ["h","e","l","l","o"," ","b","o","y","All other letters"]
segment = {
	"l": 0.20,
	"e": 0.20,
        " ": 0.10,
	"All Other Letters": 0.50
}
#window=w
w = turtle.Screen()
w.setup(450,650) #width,height
w.bgcolor("light blue")
w.title ("Probability of Letter Pie Chart")

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

turtle.penup()
turtle.right(90)
turtle.forward(r*1.33)
turtle.left(90)

for n in segment:
    turtle.pencolor('black')
    angle=piesections(segment[n])
    turtle.circle(r*1.33,angle/2)
    turtle.write("%s, %f" % (n, segment[n]), align = "center",font=('Arial',9,"bold"))
    turtle.circle(r*1.33,angle/2)







