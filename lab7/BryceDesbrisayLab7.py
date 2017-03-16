# CIS 117 Python Programming - Lab 7
# Bryce DesBrisay

def main():
    i = 0
    while i < 5:
        results = []
        fileName = input("Please enter the file name: ")
        with open(fileName, encoding='utf-8') as file:
            for line in file:
                line = line.rstrip()
                results.append(line)
            if all(line.isdigit() for line in results):
                if len(results) == int(results[0]):
                    print("The sum is " + str(sum(int(num) for num in results)))
                else:
                    print("Error: file contents invalid")
            else:
                print("Error: file contents invalid")
        i += 1
main()

