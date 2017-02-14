'''
Bryce DesBrisay
CIS 117 Python Programming - Lab 4
'''

oCost = float(input("Please enter the cost of your groceries: "))

if oCost > 10:
    discount = 0 
elif oCost > 60:
    discount = 0.08
elif oCost > 150:
    discount = 0.1
elif oCost > 210:
    discount = 0.12
else:
    discount = 0.14

total = discount * oCost
disP = discount * 100
percent = "{0:.2f}".format(disP)
print("You win a discount coupon of $", total, ". (", percent, "% of your purchase)")


'''

'''
