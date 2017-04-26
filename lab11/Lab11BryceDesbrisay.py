# 
# CIS 117 Python Programming - Lab 11
# By Bryce DesBrisay
# 

import urllib.request

webpage = str(urllib.request.urlopen("http://www.nasonline.org/").read())
categories = ['research', 'climate', 'evolution', 'cultural', 'leadership', 'science']

def main():
  for item in categories:
    print(item + ' appears ' + str(webpage.count(item)) + ' times.')

main()

# 
# Output:
# 
# research appears 9 times.
# climate appears 9 times.
# evolution appears 3 times.
# cultural appears 4 times.
# leadership appears 2 times.
# science appears 23 times.
# 
