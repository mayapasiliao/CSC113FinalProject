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

#segment has a different color, legend showing the letter and its probability
#central angle of section = segment, which is the prob_of_letter out of 100
#need a loop to create all the inputed segments 
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

for letters,n in segment:
    turtle.circle(r,angle)
    turtle.write((letters,n),align= 'center', font=('Arial',8,'Normal'))
    turtle.circle(r,angle)






