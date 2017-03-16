# CIS 117 Python Programming Lab 6
# Bryce DesBrisay

def validate(text):
    if text.isdigit() or text.isalpha() or '_' in text:
        return True

def main():
    results = {}
    line = 1
    with open('t6.py', encoding='utf-8') as data:
        for text in data:
            text = text.rstrip()
            if validate(text):
                if text in results:
                    results[text].append(line)
                else:
                    results[text] = [line]
            line = line + 1
    for word in results.keys():
        print(word + ": " + str(results[word]))

main()

'''
Output:

apple: [1, 11]
1: [2, 3]
ball: [4, 19]
art: [5]
dog: [6]
pen: [8, 21]
rat: [9]
4: [10]
carrot: [13]
orange: [15]
ant: [16, 17, 18]
stick: [20]
_: [22]
goodbye: [25]

'''
