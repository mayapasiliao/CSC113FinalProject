import turtle
from itertools import cycle
import math

#takes you to origin of the circle after each section
def origin(vertex):
    turtle.penup()
    turtle.setpos(vertex)
    turtle.pendown()

def piesections(segment):
    area = (2*math.pi)*segment
    return area

#getting values from file idk how to call the values
#Name_of_segment = the letters in the file
#segment = prob_of_letter (has to calculate the remaining letters not called)
COLORS = cycle(['yellow', 'green', 'red', 'cyan', 'white', 'blue', 'mediumpurple'])
Name_of_segment = ["h","e","l","l","o"," ","g","u","y","s","All other letters"]
segment = {
	"a": 0.50,
	"b": 0.10,
	"c": 0.20,
	"d": 0.60
}
#window=w
w = turtle.Screen()
w.setup(450,650) #width,height
w.title ("Pie Chart")

#Creating circle with vertex
r=150
vertex=(-0,0)
origin(vertex)
turtle.dot (7,"black") #idkkk
turtle.penup()
turtle.sety(-r)
turtle.pendown()

#segment has a different color, legend showing the letter and its probability
#in this function i have to call for back at origin
#area of segment = central angle of section/2pi
#central angle of section = segment, which is the prob_of_letter out of 100
#need a loop to create all the inputed segments 
angle_sum=0
for n in segment:
    angle=piesections(segment[n])
    turtle.fillcolor(next(COLORS))
    turtle.begin_fill()
    turtle.circle(r,angle)
    position = turtle.position()
    origin(vertex)
    turtle.end_fill()
    turtle.setpos(position)
    angle_sum += angle

turtle.circle(r, 360-angle_sum)





