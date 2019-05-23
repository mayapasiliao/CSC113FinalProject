# Written by Mayra Vazquez-Sanchez


def readFile():
    '''Reads file and returns its contents'''
    words = open("Words.txt", "r")
    contents = words.readlines()
    words.close()
    return contents


def getFrequencies(contents):
    '''Calculates frequencies of letter & sums all frequencies'''
    letters = dict()
    letter_count = 0
    whitespace_count = 0
    symbols_count = 0
    sum_of_freq_letters = 0
    
    for line in contents:
        for letter in line:
            if letter == "\t" or letter == "\n" or letter == " ":
                whitespace_count += 1
                letters['whitespace'] = whitespace_count
            elif (ord(letter) >= 33 and ord(letter) <= 47) or \
                 (ord(letter) >= 58 and ord(letter) <= 64) or \
                 (ord(letter) >= 91 and ord(letter) <= 96) or \
                 (ord(letter) >= 123 and ord(letter) <=126):
                symbols_count += 1
                letters['symbols'] = symbols_count 
            else:
                letter_count += 1
                letters[letter] = letters.get(letter, 0) + 1
        sum_of_freq_letters = whitespace_count + symbols_count + letter_count
    return letters, sum_of_freq_letters


def getProbability(letters, sum_of_freq_letters):
    '''Calculates probability of letter & sums all probabilities'''
    sum_probabilities = 0
    
    for letter, freq_letter in letters.items():
        prob_of_letter = freq_letter / sum_of_freq_letters
        sum_probabilities += prob_of_letter    
    return sum_probabilities


def probability():
    '''Calls all functions collectively'''
    contents = readFile()
    letters, sum_of_freq_letters = getFrequencies(contents)
    sum_probabilities = getProbability(letters, sum_of_freq_letters)
    return sum_probabilities, letters

