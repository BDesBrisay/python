# CIS 117 Python Programming - Lab 13 - Abbreviation Converter
# By Bryce DesBrisay
# Please replace: Lab 5

import string

fileName = 'testabbrev.txt'
count = 0
dictionary = {}

with open(fileName) as text:
    for line in text:
        data = line.split(':')
        dictionary[data[0]] = data[1]

while(count < 5):
    abbrev = input('Enter a message to be translated: \n')

    punct = ''
    for char in abbrev:
        if char in string.punctuation:
            punct = char
            abbrev = abbrev.replace(char, '')

    expanded = str(dictionary.get(abbrev))
    output = str(expanded + punct).replace('\n', '')

    print('The translated text is:\n' + output + '\n')
    count += 1

'''

Enter a message to be translated:
car
The translated text is:
None

Enter a message to be translated:
ttyl
The translated text is:
talk to you later

Enter a message to be translated:
app!
The translated text is:
application!

Enter a message to be translated:
idk
The translated text is:
I don't know

Enter a message to be translated:
wut
The translated text is:
what

'''
