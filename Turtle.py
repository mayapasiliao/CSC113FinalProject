import turtle
import math

#window=w
w = turtle.Screen()
w.setup(450,650,0,0) #width,height
w.title ("Pie Chart")

#getting values from file idk how to call the values
#Name_of_segment = the letters in the file
#segment = prob_of_letter (has to calculate the remaining letters not called)
#example hello guys = 10 is in file
Name_of_segment = ["h","e","l","l","o"," ","g","u","y","s","All other letters"]
segment = [0.10,0.10,0.20,0.60]


#Creating circle
r=150
vertex=-0,150
turtle.circle (r)

#makes the dot at the origin of the circle
turtle.penup()
turtle.setpos(vertex)
turtle.dot (10,"black")


#takes you to origin of the circle after each section
def origin(vertex):
    turtle.penup()
    turtle.setpos(vertex)
    

#segment has a different color, legend showing the letter and its probability
#in this function i have to call for back at origin
#area of segment = central angle of section/2pi
#central angle of section = segment, which is the prob_of_letter

def piesections(segment):
    area=segment/(2*math.pi)
    



#calling for function
piesections(segment)
