# Written by Mayra Vazquez-Sanchez


def readFile():
    '''Reads file and returns its contents'''
    words = open("Words.txt", "r")
    contents = words.readlines()
    print(contents)
    return contents

def getFrequencies(contents):
    '''Calculates frequencies of letter & sums all frequencies'''
    letters = dict()
    letter_count = 0
    sum_of_freq_letters = 0
    for line in contents:
        for letter in line:
            letters[letter] = letters.get(letter, 0) + 1
            letter_count += 1
        sum_of_freq_letters += letter_count
    print(letters)
    print(sum_of_freq_letters)
    return letters, sum_of_freq_letters

def getProbability(letters, sum_of_freq_letters):
    '''Calculates probability of letter & sums all probabilities'''
    sum_probabilities = 0
    for letter, letter_count in letters.items():
        prob_of_letter = letter_count / sum_of_freq_letters
        print(letter)
        print(prob_of_letter)
        sum_probabilities += prob_of_letter
    return sum_probabilities

def probability():
    '''Calls all functions collectively'''
    contents = readFile()
    letters, sum_of_freq_letters = getFrequencies(contents)
    sum_probabilities = getProbability(letters, sum_of_freq_letters)
    return sum_probabilities, letters

probability()
