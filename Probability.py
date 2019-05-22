# Written by Mayra Vazquez-Sanchez

def readFile():
    words = open("Words.txt", "r")
    contents = words.readlines()
    print(contents)
    return contents

def getFrequencies(contents):
    letters = dict()
    letter_count = 0
    sum_of_freq_letters = 0
    for line in contents:
        for letter in line:
            letters[letter] = letters.get(letter, 0) + 1
            letter_count++ 
        sum_of_freq_letters += letter_count
    return letters, sum_of_freq_letters

def getprobabilty(letters, sum_of_freq_letters):
    probabilities_letters = []
    probability_letter = 

