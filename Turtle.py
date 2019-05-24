import turtle
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
    Rainbow = cycle(['red','orange', 'yellow', 'light green', 'blue', 'purple', 'pink'])
    All_others = ['gray']
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
        print("%s, %f" % (x, segment[x]))
        sum_probabilities += segment[x]

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
    counter = 0
    for x in segment:
        angle=piesections(segment[x]/sum_probabilities)
        turtle.fillcolor(next(Rainbow))
        turtle.begin_fill()
        turtle.circle(r,angle)
        position = turtle.position()
        origin(vertex)
        turtle.end_fill()
        turtle.setpos(position)
        angle_sum += angle
        counter += 1
        if counter == n:
            break

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

    for x in segment:
        turtle.pencolor('black')
        angle=piesections(segment[x]/sum_probabilities)
        turtle.circle(r*1.33,angle/2)
        turtle.write("%s, %f" % (x, segment[x]), align = "center",font=('Arial',9,"bold"))
        turtle.circle(r*1.33,angle/2)
