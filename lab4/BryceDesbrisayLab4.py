'''
Bryce DesBrisay
CIS 117 Python Programming - Lab 4
'''

oCost = float(input("Please enter the cost of your groceries: "))

def calcDiscount(oCost):
    if oCost < 10:
        return 0 
    elif 10 <= oCost < 60:
        return 0.08
    elif 60 <= oCost < 150:
        return 0.1
    elif 150 <= oCost < 210:
        return 0.12
    elif 210 <= oCost:
        return 0.14

total = str("{0:.2f}".format(calcDiscount(oCost) * oCost))
percent = str(round(calcDiscount(oCost) * 100))
print("You win a discount coupon of $" + total + ". (" +
percent + "% of your purchase)")

'''
Please enter the cost of your groceries: 6.23
You win a discount coupon of $0.00. (0% of your purchase)

Please enter the cost of your groceries: 19.04
You win a discount coupon of $1.52. (8% of your purchase)

Please enter the cost of your groceries: 86.53
You win a discount coupon of $8.65. (10% of your purchase)

Please enter the cost of your groceries: 197.71
You win a discount coupon of $23.73. (12% of your purchase)

Please enter the cost of your groceries: 298.46
You win a discount coupon of $41.78. (14% of your purchase)
'''
