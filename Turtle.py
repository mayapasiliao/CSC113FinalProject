import turtle
from collections import OrderedDict
from itertools import cycle
from Probability import probability

def origin():
    turtle.penup()
    turtle.setpos(0,0)
    turtle.pendown()

def pie_sec(prob_letter):
    return 360 * prob_letter

def draw_pie_chart(n):
    rainbow = cycle(['tomato', 'orange', 'light blue', 'light gray', 'rosybrown', 'light pink','navy'])

    letters, probabilities = probability()
    letters_desc = OrderedDict(sorted(letters.items(), key=lambda \
                                      element: element[1], reverse=True))

    window = turtle.Screen()
    window.setup(700, 600)
    window.bgcolor("white")
    window.title("Probability of Most Frequent Letters")

    r = 150
    origin()
    turtle.dot(7, "black")
    turtle.penup()
    turtle.sety(-r)
    turtle.pencolor("black")
    turtle.pendown()
    
    angle_sum = 0

    for letter, letter_freq in zip(letters_desc, range(0,n)):
        c_angle = pie_sec(probabilities[letter])
        turtle.fillcolor(next(rainbow))
        turtle.begin_fill()
        turtle.circle(r,c_angle)
        pos = turtle.position()
        origin()
        turtle.end_fill()
        turtle.setpos(pos)
        angle_sum += c_angle

    rest = 360 - angle_sum
    turtle.color('lightsteelblue')
    turtle.begin_fill()
    turtle.circle(r, rest)
    pos = turtle.position()
    origin()
    turtle.end_fill()

    turtle.penup()
    turtle.right(90)
    turtle.forward(r*1.25)
    turtle.left(90)

    sum_of_prob_others = 0
    
    for letter, freq_letter in zip(letters_desc, range(0,n)):
        turtle.pencolor('black')
        c_angle = pie_sec(probabilities[letter])
        turtle.circle(r*1.25,c_angle/2)
        
        
    #   turtle.write("%s, \n %f" % (letter, probabilities[letter]), align = "center",font=('Arial',8,"bold"))
        if letters[letter]>1:
            turtle.write("%s\n" % (letter), align = "center",font=('Arial',9,"bold"))
            turtle.write("%f" % ( probabilities[letter]), align = "center",font=('Arial',9,"bold"))
        else:
            turtle.write("%s\n" % (letter), align = "center",font=('Arial',9,"bold"))
            turtle.write("%f" % ( probabilities[letter]), align = "center",font=('Arial',6,"bold"))
        turtle.circle(r*1.25,c_angle/2)
        sum_of_prob_others += probabilities[letter]
        
    turtle.circle(r*1.3,rest/2)

    if  sum_of_prob_others != 1:
          turtle.write("All other letters,\n%f" % (1-sum_of_prob_others), align = "center",font=('Arial',9,"bold"))
          turtle.circle(r*1.3,c_angle/2)

    turtle.ht()

