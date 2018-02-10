


def StartCalculator():

    num1 = float(input("Enter a number :"))

    print("")

    num2 = float(input("Enter another number :"))

    print("")

    operation = input("Enter '+' for addition, '-' for subtraction, '*' for multiplication, and '/' for division,")



    if operation == '+':

            answer = (num1 + num2)

            print("")

            print(answer)

    elif operation == '-':

            answer = (num1 - num2)

            print("")

            print(answer)

    elif operation == '*':

            answer = (num1 * num2)

            print("")

            print(answer)

    elif operation == '/':

            answer = (num1 / num2)

            print("")

            print(answer)

while(True):
    StartCalculator()
