import turtle
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
#example hello guys = 10 is in file
Name_of_segment = ["h","e","l","l","o"," ","g","u","y","s","All other letters"]
segment = {
	"a": 0.10,
	"b": 0.10,
	"c": 0.20,
	"d": 0.60
}
    
#window=w
w = turtle.Screen()
w.setup(450,650,0,0) #width,height
w.title ("Pie Chart")

#Creating circle
r=150
vertex=-0,150
turtle.circle (r)

#makes the dot at the origin of the circle
turtle.penup()
turtle.setpos(vertex)
turtle.dot (10,"black")

#segment has a different color, legend showing the letter and its probability
#in this function i have to call for back at origin
#area of segment = central angle of section/2pi
#central angle of section = segment, which is the prob_of_letter out of 100
#need a loop to create all the inputed segments 

for n in segment:
    angle=piesections(segment["a"])
    origin(vertex)
    turtle.right(angle)
    turtle.forward (150)
    origin(vertex)








