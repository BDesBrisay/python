# CIS 117 Python Programming - Lab 10
# Bryce DesBrisay

def middle(string):
    characters = list(string)
    length = len(characters)
    middleNum = round((length + .5) / 2)
    if length % 2 == 0:
        return characters[middleNum - 1] + characters[middleNum]
    else:
        return characters[middleNum - 1]

def countVowels(string):
    count = 0
    vowels = ['a','e','i','o','u','y']
    for vowel in vowels:
        count += string.count(vowel)
    return count

def reverse(string):
    return string[::-1]

def isPalindrome(string):
    return reverse(string) == string

def main():
    count = 5
    while count > 0:
        string = input('Enter a string: ')
        print('The middle character(s) is/are: ' +  middle(string))
        print('The string reversed is: ' + reverse(string))
        print('The string contains ' + str(countVowels(string)) + ' vowels.')
        if isPalindrome(string):
            print('That is a palindrome.\n')
        else:
            print('That is not palindrome.\n')
        count -= 1

main()

'''
Enter a string: racecar
The middle character(s) is/are: e
The string reversed is: racecar
The string contains 3 vowels.
That is a palindrome.

Enter a string: apple
The middle character(s) is/are: p
The string reversed is: elppa
The string contains 2 vowels.
That is not palindrome.

Enter a string: civic
The middle character(s) is/are: v
The string reversed is: civic
The string contains 2 vowels.
That is a palindrome.

Enter a string: bottle
The middle character(s) is/are: tt
The string reversed is: elttob
The string contains 2 vowels.
That is not palindrome.

Enter a string: noon
The middle character(s) is/are: oo
The string reversed is: noon
The string contains 2 vowels.
That is a palindrome.
'''

