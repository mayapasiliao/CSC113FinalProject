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
<<<<<<< HEAD
    rainbow = cycle(['tomato', 'orange', 'light blue', 'light gray', 'rosybrown', 'light pink','navy'])
=======
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
>>>>>>> 771b931fc62090a86fc659c66157824bfd8c31ac

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
    turtle.pencolor("white")
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

<<<<<<< HEAD
    rest = 360 - angle_sum
    turtle.color('lightsteelblue')
=======
    rest=360-angle_sum
    
    turtle.color(next(Rainbow))
>>>>>>> 771b931fc62090a86fc659c66157824bfd8c31ac
    turtle.begin_fill()
    turtle.circle(r, rest)
    pos = turtle.position()
    origin()
    turtle.end_fill()

    turtle.penup()
    turtle.right(90)
    turtle.forward(r*1.25)
    turtle.left(90)

<<<<<<< HEAD
    sum_of_prob_others = 0
    
    for letter, freq_letter in zip(letters_desc, range(0,n)):
        turtle.pencolor('black')
        c_angle = pie_sec(probabilities[letter])
        turtle.circle(r*1.25,c_angle/2)
        turtle.write("%s, %f" % (letter, probabilities[letter]), align = "center",font=('Arial',9,"bold"))
        turtle.circle(r*1.25,c_angle/2)
        sum_of_prob_others += probabilities[letter]
        
    turtle.circle(r*1.3,rest/2)

    if  sum_of_prob_others != 1:
          turtle.write("All other letters,\n%f" % (1-sum_of_prob_others), align = "center",font=('Arial',9,"bold"))
          turtle.circle(r*1.3,c_angle/2)
=======
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
    
>>>>>>> 771b931fc62090a86fc659c66157824bfd8c31ac


