import turtle
import operator
import collections
from itertools import cycle
from Probability import probability

#takes you to origin of the circle after each section
def origin(vertex):
    turtle.penup()
    turtle.setpos(vertex)
    turtle.pendown()
#we need to divde this by the total
def piesections(segment):
    area = (360)*segment #central angle
    return area

def draw_pie_chart(n):
    #Name_of_segment = the letters in the file
    #segment = prob_of_letter (has to calculate the remaining letters not called)
    Rainbow = cycle(['red','orange', 'yellow', 'light green', 'blue', 'purple', 'violet','gray','brown','beige'])
    Rainbow_letters = cycle(['red','orange', 'yellow', 'light green', 'blue', 'purple', 'violet','gray','brown','beige'])

    # Name_of_segment = ["h","e","l","l","o"," ","b","o","y","All other letters"]
    # segment = {
    # 	"l": 0.20,
    # 	"e": 0.20,
    #         " ": 0.10,
    # 	"All Other Letters": 0.50
    # }
    sum_probabilities, segment = probability()
    sum_probabilities = 0
    for x in segment:
        sum_probabilities += segment[x]

    sorted_segment_tuples = sorted(segment.items(), key=lambda element: element[1])
    sorted_segment_tuples.reverse()
    sorted_segment = collections.OrderedDict(sorted_segment_tuples)
    for x in sorted_segment:
        print("%s, %f" % (x, sorted_segment[x]))

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
    turtle.pencolor("white")
    turtle.pendown()

    angle_sum=0
    for (x,i) in zip(sorted_segment, range(0,n)):
        angle=piesections(segment[x]/sum_probabilities)
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

    AOL=0
    for (x,i) in zip(sorted_segment, range(0,n)):
        turtle.pencolor('black')
        angle=piesections(segment[x]/sum_probabilities)
        turtle.circle(r*1.33,angle/2)
        turtle.write("%s, %f" % (x, segment[x]/sum_probabilities)  , align = "center",font=('Arial',9,"bold"))
        turtle.circle(r*1.33,angle/2)
        AOL+=(segment[x]/sum_probabilities)

        
    turtle.pencolor('white')
    turtle.circle(r*1.33,rest/2)


    if AOL !=1:
          turtle.write('All other letters,', align = "left",font=('Arial',8,"bold"))
          turtle.forward(37)
          turtle.write((1-AOL), align = "left",font=('Arial',9,"bold"))
          turtle.circle(r*1.33,angle/2)
    

  

  
        
