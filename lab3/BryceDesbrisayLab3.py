'''
Bryce DesBrisay
CIS 117 Python Programming - Lab 3
'''

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");

dateInit = raw_input("Enter a date in the mm/dd/yyyy format: ")
date = dateInit.split("/");

monthInt = int(date[0]) - 1;

print( months[monthInt] + " " + date[1] + ", " + date[2]);

'''
Enter a date in the mm/dd/yyyy format: 01/01/1999
January 01, 1999
'''
