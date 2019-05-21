# Written by Mayra Vazquez-Sanchez

def readFile():
    words = open("Words.txt", "r")
    contents = words.readlines()
    letters = {}
    letter_count = 0
    for line in contents:
        for letter in line:
            letter_count = 
