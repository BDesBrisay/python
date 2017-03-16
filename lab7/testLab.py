# CIS 117 Python Programming - Lab 7
# Bryce DesBrisay

def main():
    runs = 0
    while runs < 5:
        results = []
        filename = raw_input("Please enter the file name: ")
        with open(filename, encoding='utf-8') as data:
            for item in data:
                item = item.rstrip()
                results.append(item)
            if all(item.isdigit() for item in results):
                if len(results) == int(results[0]):
                    print("The sum is " + str(sum(int(num) for num in results)))
                else:
                    print("Error: file contents invalid.")
            else:
                print("Error: file contents invalid.")
        runs += 1

main()
